import sqlite3, re
from pprint import pprint
import Levenshtein

def search(sign):
  sign = re.sub('^/+', '', sign)
  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT id,url FROM exploits WHERE description like ?", ('%'+sign+'%',))
  res = c.fetchall()
  conn.commit()
  conn.close()
  
  arr = {}
  for item in res:
    arr[item[0]] = item[1]
  
  return arr

def search_path(sign):
  sign = re.sub('^/+', '', sign)
  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT id,url FROM exploits WHERE path like ?", ('%'+sign+'%',))
  res = c.fetchall()
  conn.commit()
  conn.close()
  
  arr = {}
  for item in res:
    arr[item[0]] = item[1]
  
  return arr


def search_path_exact(sign):
  sign = re.sub('^/+', '', sign)
  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT id,url FROM exploits WHERE path like ?", [sign])
  res = c.fetchall()
  conn.commit()
  conn.close()
  
  arr = {}
  for item in res:
    arr[item[0]] = item[1]
  
  return arr

def fuzzy_search(sign, score=0.9):
  sign = re.sub('^/+', '', sign)
  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT id,url,path FROM exploits")
  res = c.fetchall()
  conn.commit()
  conn.close()
  arr = {}
  for item in res:
    if(Levenshtein.jaro_winkler(sign, item[2]) > score):
      arr[item[0]] = item[1]
  return arr