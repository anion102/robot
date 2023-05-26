# encoding=utf-8
# author: Jenny Kan
import json

import requests


def req_get(url, param=None, header={'content-type': 'application/json'}):
    r = requests.get(url=url, params=param,headers=header)
    return r.text


def req_post(url, data, header={'content-type': 'application/json'}):
    r = requests.post(url=url, data=json.dumps(data), headers=header)
    return r.text
