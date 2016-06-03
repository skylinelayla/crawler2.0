# -*- coding: utf-8 -*-

import sys
from lxml import html
from lxml import etree


reload(sys)
sys.setdefaultencoding("utf-8")

import requests

class Spider():
    def __init__(self,url,option="print_data_out"):
        self.url=url
        self.option=option
        self.header={}

        #cookie
        self.header["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0"
        self.cookies={"q_c1":"8074ec0c513747b090575cec4a547cbd|1459957053000|1459957053000",
                      "l_cap_id":'"Y2MzODMyYjgzNWNjNGY4YzhjMDg4MWMzMWM2NmJmZGQ=|1462068499|cd4a80252719f069cc467a686ee8c130c5a278ae"',
                      "cap_id":'"YzIwNjMwNjYyNjk0NDcyNTkwMTFiZTdiNmY1YzIwMjE=|1462068499|efc68105333307319525e1fc911ade8151d9e6a6"',
                      "d_c0":'"AGAAI9whuwmPTsZ7YsMeA9d_DTdC6ijrE4A=|1459957053"',
                      "_za":"9b9dde53-9e53-4ed1-a17f-363b875a8107",
                      "login":'"YWQyYzQ4ZDYyOTAwNDVjNTg2ZmY3MDFkY2QwODI5MGY=|1462068522|49dd99d3c8330436f211a130209b4c56215b8ec3"',
                      "__utma":"51854390.803819812.1462069647.1462069647.1462069647.1",
                      "__utmz":"51854390.1462069647.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
                      "_xsrf":"6b32002d2d529794005f7b70b4ad163e",
                      "_zap":"a769d54e-78bf-44af-8f24-f9786a00e322",
                      "__utmb":"51854390.4.10.1462069647",
                      "__utmc":"51854390",
                      "l_n_c":"1",
                      "z_c0":"Mi4wQUFBQWNJQW9BQUFBWUFBajNDRzdDUmNBQUFCaEFsVk5LdkpNVndCRlQzM1BYVEhqbWk0VngyVkswSVdpOXhreDJB|1462068522|eed70f89765a9dd2fdbd6ab1aabd40f7c23ea283",
                      "s-q":"%E4%BA%91%E8%88%92",
                      "s-i":"2",
                      "sid":"1jsjlbsg",
                      "s-t":"autocomplete",
                      "__utmv":"51854390.100--|2=registration_date=20140316=1^3=entry_date=20140316=1",
                      "__utmt":"1"}

    def get_user_data(self):
        followee_url=self.url
        get_html=requests.get(followee_url,cookies=self.cookies,headers=self.header,verify=False)
        return get_html.text

    def clean_data(self,htmltext):
        selector=html.fromstring(htmltext)
        #提取link元素
        content=selector.xpath('//link/@href')
        for each in content:
            print(each)
        #提取meta中的属性
        meta=selector.xpath('//meta')
        for each in meta:
            print(each)
        #提取title
        title=selector.xpath('//title')
        for each in title:
            print(title)



spider=Spider("http://www.zhihu.com","print_data_out")
spider.clean_data(spider.get_user_data())


