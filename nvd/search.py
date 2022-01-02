import requests, json, re

def search(sign):

  sign = re.sub('^/+', '', sign)
  url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
  payload = {"keyword":sign}
  res_json = requests.get(url, params=payload)
  res = json.loads(res_json.text)

  if res["resultsPerPage"]!=0:
    arr = {}
    for item in res["result"]["CVE_Items"]:
      cve = item["cve"]["CVE_data_meta"]["ID"]
      arr[cve] = 'https://nvd.nist.gov/vuln/detail/'+cve
    return arr
  else:
    return []