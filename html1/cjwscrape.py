# 2017 Mar 17
# Li Yuqiong
# Task: scrap a table from URL http://www.cjw.gov.cn/zwzc/bmgb/

import requests, bs4
res = requests.get("http://www.cjw.gov.cn/zwzc/bmgb/")
res.raise_for_status()
total = bs4.BeautifulSoup(res.text)

# from_encoding="UTF-8"

# html = urllib2.urlopen("http://www.515fa.com/che_1978.html")
# content = html.read().decode('utf-8', 'ignore')
# soup = BeautifulSoup(content)

elems = total.select(".left a")
# elems is a list of all class = ".left" objects where the <a> tag
# Note previously had a bug when only select ".left"
len(elems) # 58 elements in elems
type(elems) # elems is a list
type(elems[0])
elems[0].getText() # here get the title but encodings are problematic
str(elems[0])  # then you get a string! of elems[0]
elems[0].attrs
elems[0].get('href')

res = requests.get(elems[0].get('href'))
# An output python function
def outFile(res, name): # res is a request response object, name is a string
    outFile = open(name+'.html', 'wb')
    for chunk in res.iter_content(100000):  # iter_content method here
        outFile.write(chunk)
    outFile.close

# Serious code
# Find the URL for pages
elems = total.select(".left a")
    for i in range(len(elems)):
        url = "http://www.cjw.gov.cn/"+elems[i].get('href')
        res = requests.get(url)
        res.raise_for_status()
        outFile(res, "page"+str(i))

# Till now have gotten all the html pages
