#coding=utf-8
import urllib2
from city import city
import json

cityname = raw_input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
   url = 'http://wthrcdn.etouch.cn/WeatherApi?citykey=%s' % citycode
   content = urllib2.urlopen(url).read()
print content
