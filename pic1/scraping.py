#! python
# 2017 Mar 18
# Li Yuqiong
# Task: scrape all pictures from http://www.yellowriver.gov.cn/other/hhgb/

import requests

def outImage(res, name): # res is a request response object, name is a string
    outImage = open(name+'.jpg', 'wb')
    for chunk in res.iter_content(100000):  # iter_content method here
        outImage.write(chunk)
    outImage.close
# Note here even if it's an image request still reads by chunk

# For year 2015
for i in range(2013, 2016):
    for j in range(45):
        url = "http://www.yellowriver.gov.cn/other/hhgb/"+str(i)+"szygb/files/mobile/"+str(j)+".jpg"
        res = requests.get(url)
        if res.status_code == 404:
            print("The link for year = "+str(i)+ " and No. = " + str(j) + " is not found.")
        else:
            outImage(res, "y"+str(i)+"no"+str(j))
