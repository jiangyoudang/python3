#-*- coding:utf-8 -*-
from os import listdir, mkdir
import urllib.parse

from bs4 import BeautifulSoup
import requests

import time

time_start = time.time()

def save_img_html(url,content=None):
    url = urllib.parse.unquote(url)
    title = url.split('/')[-1]
    type_ = title.split('.')[-1]
    if type_=='html':
        # if 'wiki' not in listdir('.'):
        #     mkdir('./wiki')
        # if title not in listdir('./wiki'):
        #     with open('wiki/{}'.format(title),'wb') as html:
        #         html.write(content)
        with open('wiki/{}'.format(title),'wb') as html:
                html.write(content)
    else:
        # image
        # if 'wiki' not in listdir('.'):
        #     mkdir('./wiki')
        # if 'img' not in listdir('./wiki'):
        #     mkdir('./wiki/img')
        if title not in listdir('./wiki/img'):
            content = requests.get(url).content
            with open('wiki/img/{}'.format(title),'wb') as img_write:
                img_write.write(content)

if 'wiki' not in listdir('.'):
    mkdir('./wiki')
if 'img' not in listdir('./wiki'):
    mkdir('./wiki/img')

root_url = "http://dont-starve-game.wikia.com/"
apis = {'article_list':"api/v1/Articles/List?limit=25000",
        'article_content_simple': 'api/v1/Articles/AsSimpleJson?id={id}',
        }

articles_list_r = requests.get(root_url+apis['article_list'])
articles_list = articles_list_r.json()

with open('download_list.txt','wb') as f:
    for article in articles_list['items']:
        f.write('\n'.encode())
        for key,value in article.items():
            f.write('{}:{}, '.format(key,value).encode())

#write index.html
pattern = '<td width="10%"><a href="{}">{}</a></td>'
with open('wiki/index.html','wb') as f:
    f.write('<table>'.encode())
    i=0
    article_num = len(articles_list['items'])
    while(i<article_num):
        f.write('<tr>'.encode())
        for article in articles_list['items'][i:i+10]:

            url = urllib.parse.unquote(article['url'])
            href = url.split('/')[-1]+'.html'
            title = article['title']
            f.write(pattern.format(href,title).encode())

        f.write('</tr>'.encode())
        i += 10
    f.write('</table>'.encode())

basepath = articles_list['basepath']
for article_info in articles_list['items']:

    article_url = article_info['url']
    article_title = article_info['title']
    print('downloading: '+article_title)

    r = requests.get(basepath+article_url)
    soup = BeautifulSoup(r.text)
    content = soup.find('div','mw-content-ltr')

    #remove edit class
    edits = content.find_all(class_='editsection')
    for edit in edits:
        edit.decompose()

    all_links = content.find_all('a')
    all_link_span = content.find_all('span')
    all_links.extend(all_link_span)

    for link in all_links:
        if link.find('noscript'):
            new_content = link.noscript.contents[0]
            link.clear()
            link.append(new_content)
        if link.get('href'):
            href = link['href']
            new_href = href.split('/')[-1]+'.html'
            link['href'] = new_href

    all_img = content.find_all('img')
    for img in all_img:
        src = img.get('src')
        if src:
            src_split = src.split('/')
            img_name = src_split[-1]
            img_link_prefix = src_split[0]
            if img_link_prefix=='http:':
                save_img_html(src)
                img['src'] = 'img/{}'.format(img_name)
    save_img_html(article_url+'.html',content.encode())
    # print(article_url)
# print(len(articles_list['items']))
# print(content)
time_end = time.time()

print('time used: {} s'.format(time_end-time_start))