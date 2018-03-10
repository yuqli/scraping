# 2017 Mar 14
# Yuqiong Li
import requests, bs4
res = requests.get("http://www.ipe.org.cn/MapWater/water.aspx?q=2")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(noStarchSoup)

noStarchSoup.select("#leftdiv_hchcontent_content")
# The codes above do not work because the elements are not in the source codes
# the elements are retrived from javascript from a database

# use request to send post data to the server
# Address is http://www.ipe.org.cn/data_ashx/GetAirData.ashx

r = requests.post("http://www.ipe.org.cn/data_ashx/GetAirData.ashx",
... data={ headers: { 'Cookie': document.cookie }, cmd: 'gethch_content',
... mid: 7721
... })


{"isSuccess":1,"Content":"%20%3Cdiv%20class%3D%22side-con%22%3E%0D%0A%3Cdiv%20class%3D%22section-info%22%3E%0D%0A%3Cdiv%20class%3D%22table-con%20table-selection%22%3E%0D%0A%3Cdiv%20class%3D%22table-main%22%3E%0D%0A%3Ctable%20class%3D%22table-list%22%3E%0D%0A%3Ctbody%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u7A0B%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u8F7B%u5EA6%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6240%u5728%u5730%u533A%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u6E56%u5317-%u6B66%u6C49%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u6CB3%u6BB5%u8D77%u70B9%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u4E09%u773C%u6865%u95F8%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9ED1%u81ED%u6CB3%u6BB5%u7EC8%u70B9%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u6F6D%u6D32%u666F%u95F8%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u957F%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A2.833%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u9762%u79EF%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u8D23%u4EFB%u4EBA%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u5218%u7ACB%u65B0%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u7535%u8BDD%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6CBB%u7406%u65F6%u9650%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u6F6D%u6D32%u666F%u95F8%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Cth%3E%0D%0A%u6CBB%u7406%u8FDB%u5EA6%0D%0A%3C/th%3E%0D%0A%3Ctd%20class%3D%22text-left%22%3E%0D%0A%u6CBB%u7406%u4E2D%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3Ctr%3E%0D%0A%3Ctd%20colspan%3D%222%22%20class%3D%22text-left%20water-pic-case%22%3E%0D%0A%3Cdiv%20class%3D%22water-pic%22%20id%3D%22pic_list%22%3E%0D%0A%3Cul%20class%3D%22clearfix%22%3E%0D%0A%3C/ul%3E%0D%0A%3C/div%3E%0D%0A%3C/td%3E%0D%0A%3C/tr%3E%0D%0A%3C/tbody%3E%0D%0A%3C/table%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A%3Cdiv%20class%3D%22side-source%22%3E%0D%0A%3Cp%3E%0D%0A%u6570%u636E%u6765%u6E90%3A%u5168%u56FD%u57CE%u5E02%u9ED1%u81ED%u6C34%u4F53%u6574%u6CBB%u4FE1%u606F%u5E73%u53F0%3C/p%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A%3C/div%3E%0D%0A","MName":"朱家老港"}
