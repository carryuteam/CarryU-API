# -*- coding: utf-8 -*-
import requests
import json


class WXLogin:
    def __init__(self, appid, secret):
        self.appid = appid
        self.secret = secret
        print(appid)
        print(secret)

    def login(self, code):
        url = "https://api.weixin.qq.com/sns/jscode2session"
        param = {
            "grant_type": 'authorization_code',
            "appid": self.appid,
            "secret": self.secret,
            "js_code": code
        }
        ret = requests.get(url, params=param)
        print(ret.text)
        ret = json.loads(ret.text)
        return ret
