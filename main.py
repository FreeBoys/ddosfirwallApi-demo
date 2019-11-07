#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import xmltodict
class Status:
    User = ""
    Pass = ""

    DomainUrl = ""
    Login = "/cgi-bin/login.cgi"
    ServiceVersion = "/cgi-bin/service_version.cgi"
    StatusGlobal = "/cgi-bin/status_global.cgi"
    StatusHealth = "/cgi-bin/status_health.cgi"
    StatusPranges = "/cgi-bin/status_pranges.cgi"


    #获取cookie的sid值
    def getSid(self):
        url = self.DomainUrl + self.Login
        values = {'param_type':"login", 'param_username':self.User, 'param_password':self.Pass}
        req = requests.post(url, values)
        cookieVa = req.cookies
        sid = 'sid=' + cookieVa._find('sid')
        return sid


    def run(self,sid):
        sid = sid
        headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Cookie" : sid}
        #获取全局状态
        respons = requests.get(self.DomainUrl + self.StatusGlobal, headers = headers)
        #取得xml解析成json格式
        json = xmltodict.parse(respons.text)
        print(json['status_global']['wan_input_bps'])


if __name__ == '__main__':
    ddosFirwall = Status()
    sid = ddosFirwall.getSid()
    ddosFirwall.run(sid)