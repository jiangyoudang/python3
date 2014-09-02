import requests
from bs4 import BeautifulSoup

f = open('kunlun.txt','w')

url = 'http://www.sbkk8.cn'

page  ='/wangluo/kunlun/162561.html'
nextpage = page

while(nextpage):
    r = requests.get(url+nextpage)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text)
    article = soup.find('div','f_article').find_all('p')
    title = soup.find('div',{'id':'f_title'})
    nextpage_div = soup.find('div','mingzhuPage')
    nextpage = nextpage_div.find('a','nextPage')
    if nextpage:
        nextpage = nextpage['href']

    f.write(title.h1.string+'\n')
    print('downloading ... {}'.format(title.h1.string))
    for line in article:
        if line.find('img'):
            line.img.extract()
        f.write(str(line.string)+'\n')
    f.write('\n\n')



f.close()

