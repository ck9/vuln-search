from functions import get_option
from pprint import pprint

opts = get_option()

sign = input('Enter Signature : ')

# デフォルトではパスのみ検索 -qオプション指定でクエリ含めて検索
if(not opts.querySearch):
  sign = sign.split("?")[0]

print("nvd")
from nvd.search import search as search_nvd
pprint(search_nvd(sign))

print("exploitdb")
from exploitdb.search import search as search_edb
pprint(search_edb(sign))

print("vulners")
from vulners_.search import search as search_vulners
pprint(search_vulners(sign))

print("cnvd")
from cnvd.search import search as search_cnvd
pprint(search_cnvd(sign))
