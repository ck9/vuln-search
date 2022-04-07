from unittest import result
from src.functions import *
from pprint import pprint

opts = getOption()

sign = input('Enter Signature : ')

# デフォルトではパスのみ検索 -qオプション指定でクエリ含めて検索
if not opts.querySearch:
  sign = sign.split("?")[0]

count = opts.count

from src.nvd.search import search as search_nvd
from src.exploitdb.search import search as search_edb
from src.vulners_.search import search as search_vulners
from src.cnvd.search import search as search_cnvd

tagsList = makeResult([search_nvd(sign),search_edb(sign),search_vulners(sign),search_cnvd(sign)])

tagsPrint(tagsList,count)

if opts.yamlFormat:
  yamlOutput(sign,tagsList,count)
