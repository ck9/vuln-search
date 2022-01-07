from pprint import pprint

sign = input('Enter Signature : ')

print("nvd")
from nvd.search import search as search_nvd
pprint(search_nvd(sign))

print("exploitdb")
from exploitdb.search import search as search_edb
pprint(search_edb(sign))

print("vulners")
from vulners.search import search as search_vulners
pprint(search_vulners(sign))

print("vulners")
from cnvd.search import search as search_cnvd
pprint(search_cnvd(sign))
