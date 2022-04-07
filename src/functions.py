from argparse import ArgumentParser
from pprint import pprint
import yaml

def getOption():
    argparser = ArgumentParser()
    argparser.add_argument('-q', '--querySearch',
                           action='store_true',
                           help='Search path & query.')
    argparser.add_argument('-y', '--yamlFormat',
                           action='store_true',
                           help='Return YAML Format.')
    argparser.add_argument('-c', '--count',
                           action='store',
                           default=10,
                           help='Number of output. (default: 10)')
    return argparser.parse_args()

def makeResult(result):
    tagslist = {}
    n = 0
    for row in result:
        for key in row.keys():
            keyr =  key.replace("EDB-ID:","EDB-")
            tagslist[keyr] = {'count': tagslist.get(key,{'count':0})['count']+1, 'urls': tagslist.get(key,{'urls':[]})['urls'] + [row[key]]}
            n += 1
    tagslist_sorted = dict(sorted(tagslist.items(), key=lambda x:x[1]['count'], reverse=True))
    print(f'\n[INFO] {n} results.\n')
    return tagslist_sorted

def tagsPrint(tagsList,count):
    n = 1
    for key in tagsList.keys():
        isFirst = True
        print(f'No. {n}\n  tag : {key}\n  cf. :',end='')
        for url in tagsList[key]['urls']:
            if isFirst: print(f' {url}')
            else: print(f'        {url}')
            isFirst = False
        if n >= count:
            break
        n += 1

def yamlOutput(sign,tagsList,count):
    print('\n[INFO] Generate YAML format')
    if len(tagsList)==1:
        ids=[1]
    else:
        print('[INFO] Enter comma-delimited No. (e.g.: 1,3,5)')
        ids = list(map(int, input('No: ').split(',')))
    n = 1
    outputList = {'tags':[], 'memos': []}
    for key in tagsList.keys():
        if n in ids:
            outputList['tags']+=[key]
            outputList['memos']+=tagsList[key]['urls']
        if n >= count:
            break
        n += 1
    tagStr = ", ".join(outputList['tags'])
    memoStr = ", ".join(outputList['memos'])
    obj = [{'author':'', 'condition': [sign], 'memo': memoStr, 'name': tagStr, 'tag': tagStr}]
    print('\n',yaml.dump(obj))
