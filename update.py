# pip3 install cve_searchsploit
print("exploitdb")
from src.exploitdb.db_update import update as update_edb
update_edb()
print("Completed!\n")

# 1. download xml files from https://www.cnvd.org.cn/shareData/list
# 2. put xml files into /xmls/
print("cnvd")
from src.cnvd.db_update import update as update_cnvd
update_cnvd()
print("Completed!\n")
