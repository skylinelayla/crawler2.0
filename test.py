#encoding=utf-8
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf8')

text='''
<div>
    <ul>
        <li class="item-0"><a href="link.html"> first item</a> </li>
        <li class="item-1"><a href="link2.html"> second item</a> </li>
        <li class="item-inactive"><a href="link3.html"> third item</a> </li>
        <li class="item-1"><a href="link4.html"> fourth item</a> </li>
        <li class="item-0"><a href="link5.html"> fifth item</a> </li>
'''
html=etree.HTML(text)
result=html.xpath('//li/a[@href="link.html"]')
print(result)

html2=etree.parse('test.html')
result2=html2.xpath('//li//span')
print(result2)

result3=html2.xpath('//li/a//@class')
print(result3)

result4=html2.xpath('//li[last()]/a/@href')
print(result4)




