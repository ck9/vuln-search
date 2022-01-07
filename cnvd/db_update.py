# 1. download xml files from https://www.cnvd.org.cn/shareData/list
# 2. put xml files into /xmls/
# 3. python3 db_update.py

import xml.etree.ElementTree as ET
import sqlite3
import glob, os.path

data = []
xmls = glob.glob(os.getcwd()+"/xmls/*")
for xml in xmls:
  xml_tree = ET.parse(xml)
  xml_root = xml_tree.getroot()

  for child in xml_root:
    id = child.find("number").text
    source = "https://www.cnvd.org.cn/flaw/show/"+id
    cves = child.find("cves")
    if(cves):
      id = cves.find("cve").find("cveNumber").text
    description = child.find("description").text
    description = ''.join(description.split())
    data.append([id, source, description])

conn = sqlite3.connect('exploits.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS exploits (id , url text UNIQUE, description)')
c.executemany("REPLACE INTO exploits (id , url, description) VALUES(?, ?, ?)", data)
conn.commit()
conn.close()