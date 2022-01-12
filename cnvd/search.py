import sqlite3, re
from pprint import pprint

def search(sign):
  sign = re.sub('^/+', '', sign)
  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT id,url FROM exploits WHERE description like ?", ('%'+sign+'%',))
  res = c.fetchall()
  conn.commit()
  conn.close()

  return res