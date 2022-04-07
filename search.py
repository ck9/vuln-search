from src.functions import get_option
from pprint import pprint

opts = get_option()

sign = input('Enter Signature : ')

# デフォルトではパスのみ検索 -qオプション指定でクエリ含めて検索
if(not opts.querySearch):
  sign = sign.split("?")[0]

print("nvd")
from src.nvd.search import search as search_nvd
pprint(search_nvd(sign))

print("exploitdb")
from src.exploitdb.search import search as search_edb
pprint(search_edb(sign))

print("vulners")
from src.vulners_.search import search as search_vulners
pprint(search_vulners(sign))

print("cnvd")
from src.cnvd.search import search as search_cnvd
pprint(search_cnvd(sign))
