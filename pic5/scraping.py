#!python
# 2017 Mar 21
# Li Yuqiong
# Task: scrape selected pictures from http://www.hwcc.gov.cn/hwcc/wwgj/xxgb/szyzlgb/201601/t20160127_54095.html

import requests, bs4

execfile('iofunctions.py') # This imports functions outImage, getSoup

# Main page one: http://www.hwcc.gov.cn/hwcc/wwgj/xxgb/szyzlgb/index.html


# Get URL for the main page and select all the links
url = "http://www.hwcc.gov.cn/hwcc/wwgj/xxgb/szyzlgb/201601/t20160127_54095.html"
soup = getSoup(url)
elems = soup.select('p img[src*="jpg"]')

for i in range(len(elems)):
    url = "http://www.hwcc.gov.cn/hwcc/wwgj/xxgb/szyzlgb/201601/"+elems[i].get('src').replace("./", "")
    res = requests.get(url)
    if res.status_code == 404:
        print("The link for picture " + str(i+1) + " is not found.")
    else:
        outImage(res, "pic"+str(i+1))
