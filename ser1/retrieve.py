#!python
# Apr 9, 2017
# Li Yuqiong
# Try retrieving the information from server
# URL: http://www.ipe.org.cn/MapWater/water.aspx?q=2

import requests;

city = {'headers%5BCookie%5D':'__utma=105455707.300171550.1491201446.1491639588.1491648035.3; __utmc=105455707; __utmz=105455707.1491201446.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ajaxkey=AC2B9694EE5A79C4E982B97CEE5F176B6A3AD3FDDBB72E7B', 'cmd':'gethch_content', 'mid':'9720'}
r = requests.post("http://www.ipe.org.cn/data_ashx/GetAirData.ashx", data = city)
