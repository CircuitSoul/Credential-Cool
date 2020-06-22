#!/usr/bin/env python
# coding: utf-8

import re, json, sys, requests

def getCreds(url):
    print("\n(+) Getting credentials ...\n")
    targetDomain = sys.argv[1]
    proxies = {
        'http': 'socks5h://127.0.0.1:9050', 
        'https': 'socks5h://127.0.0.1:9050'
    }    
    postData = {
        'luser': '', 
        'domain': targetDomain, 
        'luseropr': 0, 
        'domainopr': 0, 
        'submitform': 'em'
    }
    r = requests.post(url, proxies=proxies, data=postData)
    return r.text

def pwndbResponseParse(response):
    print("\n(+) Parsing response data ...\n")
    resp = re.findall(r"\[(.*)", response)
    resp = [resp[n : n + 4] for n in range(0, len(resp), 4)]

    results = {}
    getinfo = lambda s: s.split("=>")[1].strip()
    for item in resp:
        results[getinfo(item[0])] = {
            "email": "{}@{}".format(getinfo(item[1]), getinfo(item[2])),
            "passw": getinfo(item[3]),
        }
    return results

def dictionaryToJson(response):
    print("\n(+) Creating creds.json file ...\n")
    j = json.dumps(response)
    with open('creds.json', 'w') as f:
        f.write(j)
        f.close()

def main():
    url = "http://pwndb2am4tzkvold.onion/"
    dictionaryToJson(pwndbResponseParse(getCreds(url)))
    
if __name__ == "__main__":
    main()