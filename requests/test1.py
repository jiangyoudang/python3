#
# #coding:utf-8
#
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
#
#
# url = 'https://www.google.com/'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
# headers = {'User-Agent':user_agent,
#            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Accept-Encoding':'gzip,deflate,sdch',
#             'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
#             'Cache-Control':'no-cache',
#             'Connection':'keep-alive',
#             'Content-Type':'text/html; charset=utf-8'}
#
# r = requests.get(url,headers=headers)
# # req = urllib.request.Request(url)
# # req.add_header(**headers)
# # r = urllib.request.urlopen(req)
#
# # opener = urllib.request.build_opener()
# # urllib.request.install_opener(opener)
# # r = urllib.request.urlopen(url)
#
# # with open('download.html','wb') as f:
# #     f.write(r.read())
#
# print(r.request.cookies)

import wiki

wiki.download_img('http://img3.wikia.nocookie.net/__cb20140408110712/dont-starve-game/images/thumb/f/f8/Reign_of_Giants_icon.png/30px-Reign_of_Giants_icon.png')