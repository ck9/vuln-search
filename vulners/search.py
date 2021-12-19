from dotenv import load_dotenv
load_dotenv()

import os, json, re
import vulners
from pprint import pprint
vulners_api = vulners.VulnersApi(api_key=os.getenv('VULNERS_APIKEY'))

sign = input('Enter Signature : ')
res = vulners_api.find_exploit_all(sign+"")
if len(res)!=0:
  arr = {}
  for item in res:
    if len(item["cvelist"])!=0:
      cve = item["cvelist"][0]
    else: 
      res = re.search(r'CVE-[0-9]+-[0-9]+',item["title"])
      if res:
        cve = res.group()
      else:
        cve = item["id"]
    arr[cve] = {'cve': cve, 'title':item["title"], 'url':item["vhref"]}
  print(arr)
else:
  print("Not Found")

  