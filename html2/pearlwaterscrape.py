#! python
# 2017 Mar 17
# Li Yuqiong
# Task: scrap a table from URL http://www.cjw.gov.cn/zwzc/bmgb/

import requests, bs4, webbrowser

def outFile(res, name): # res is a request response object, name is a string
    outFile = open(name+'.html', 'wb')
    for chunk in res.iter_content(100000):  # iter_content method here
        outFile.write(chunk)
    outFile.close

for i in range(2011, 2017): # i is for loop over diff. years
    siteurl = "http://www.pearlwater.gov.cn/sztb//"+str(i)+"tb/"
    res = requests.get(siteurl)
    res.raise_for_status()
    print(res.text[:250])

    soup = bs4.BeautifulSoup(res.text,"html.parser")
    elems = soup.select('td img ~ a[href*="htm"]') # Note the selectors here

    for j in range(len(elems)):
        url = "http://www.pearlwater.gov.cn/sztb//"+str(i)+"tb/"+elems[j].get('href').replace("./", "/")
        res = requests.get(url)
        res.raise_for_status()
#        webbrowser.open(url)
        if res.status_code != 404:
            outFile(res, "y"+str(i)+"m"+str(j+1))
