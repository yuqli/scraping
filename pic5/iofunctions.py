#!python
# 2017 Mar 18
# Li Yuqiong
# Package all the usually used functions so no need to type into command line
import requests, bs4

def outImage(res, name): # res is a request response object, name is a string
    outImage = open(name+'.jpg', 'wb')
    for chunk in res.iter_content(100000):  # iter_content method here
        outImage.write(chunk)
    outImage.close
# Note here even if it's an image request still reads by chunk

def getSoup(url): # url is the home url; pass a url and return a soup object
    res = requests.get(url)
    res.raise_for_status()
    if res.status_code == 404:
        print("404: Page is not found at this URL.")
    else:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
    return(soup)
