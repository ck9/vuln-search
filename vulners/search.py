import os, json, re
import vulners
from dotenv import load_dotenv

def search(sign):

  load_dotenv()
  vulners_api = vulners.VulnersApi(api_key=os.getenv('VULNERS_APIKEY'))

  sign = '"'+re.sub('^/+', '', sign)+'"'
  res = vulners_api.find_exploit_all(sign)
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
          res = re.search(r'CVE-[0-9]+-[0-9]+',item["title"])
          cve = item["id"]
      arr[cve] = item["vhref"]
    return arr
  else:
    return []