# 2017 Mar 9
# Li Yuqiong
# Scarpping websites for water quality data

import webbrowser
webbrowser.open('http://yuqli.com/')

# A mistake
# >>> webbrowser.open('http://yuqli.com/')
# True

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)
res.status_code == requests.codes.ok # check if the connection is fine
len(res.text)
print(res.text[:250]) # print the first 250 words

res.raise_for_status() # if connect successful do nothing; else stop
## another method
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Now write the webpage downloaded into a local file
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):  # iter_content method here
    playFile.write(chunk)
playFile.close


http://www.ipe.org.cn/MapWater/water.aspx?q=2

res = requests.get("http://www.ipe.org.cn/MapWater/water.aspx?q=2")

for chunk in res.iter_content(100000):  # iter_content method here
    sc.write(chunk)
