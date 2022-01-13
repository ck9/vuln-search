# vuln-search
command line search tools for vulnerabilities

# Usage
```bash
$ python3 search.py
```

# Installation

- install required packages
```bash
$ git clone https://github.com/ck9/vuln-search
$ cd vuln-search
$ pip3 install -r requirements.txt
```

- download xml files from CNVD onto cnvd/xmls/

  CNVD: https://www.cnvd.org.cn/shareData/list

- database update
```bash
$ python3 update.py
```

- make .env and add API keys
