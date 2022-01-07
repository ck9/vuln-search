import sqlite3
from pprint import pprint

def search(sign):

  conn = sqlite3.connect('exploits.db')
  c = conn.cursor()
  c.execute("SELECT * FROM exploits WHERE description like ?", ('%'+sign+'%',))
  res = c.fetchall()
  conn.commit()
  conn.close()

  return res