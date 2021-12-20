import requests, json

from pprint import pprint

sign = input('Enter Signature : ')
sign = re.sub('^/+', '', sign)
url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
payload = {"keyword":sign}
res_json = requests.get(url, params=payload)
res = json.loads(res_json.text)

if res["resultsPerPage"]!=0:
  arr = {}
  for item in res["result"]["CVE_Items"]:
    cve = item["cve"]["CVE_data_meta"]["ID"]
    arr[cve] = {'cve': cve, 'url':'https://nvd.nist.gov/vuln/detail/'+cve}
  print(arr)
else:
  print("Not Found")

  
  
