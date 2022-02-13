# vuln-search
command line search tools for vulnerabilities

# Usage
```
$ python3 search.py [options]

  Options:
    -h, --help          Show help message.
    -q, --querySearch   Search path & query.
```

# Installation

- install required packages
```
$ git clone https://github.com/ck9/vuln-search
$ cd vuln-search
$ pip3 install -r requirements.txt
```

- download xml files from CNVD onto cnvd/xmls/

  CNVD: https://www.cnvd.org.cn/shareData/list

- database update
```
$ python3 update.py
```

- make .env file and add API keys
