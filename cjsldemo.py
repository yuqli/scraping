# 2017 Mar 16
# Li Yuqiong
# Task: scrap a table from URL http://www.ywrp.gov.cn/zjszyzlgb/4769.html

import requests, bs4
res = requests.get("http://www.ywrp.gov.cn/zjszyzlgb/4769.html")
res.raise_for_status()
total = bs4.BeautifulSoup(res.text, from_encoding="UTF-8")
print(total.prettify())

# , "html.parser"

playFile = open('test.txt', 'wb')
for chunk in res.iter_content(100000):  # iter_content method here
    playFile.write(chunk)
playFile.close
