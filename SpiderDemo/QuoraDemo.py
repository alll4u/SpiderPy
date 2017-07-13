#!/usr/bin/env python
# encoding=utf-8

"""
爬取豆瓣电影TOP250 - 完整示例代码
"""

import codecs

import requests
from bs4 import BeautifulSoup
import pdfkit

DOWNLOAD_URL = 'https://zhuanlan.zhihu.com/p/21261262'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")

    question_list = soup.find('ol')

    # question_name_list = []
    # question_link_list = []
    # question_union = []
    question_dict = []
    for question_li in question_list.find_all('li'):

        question_unit = question_li.find('a')
        
        # question_name_list.append(question_unit.getText())
        # question_link_list.append(question_unit['href'])
        # question_union.append([question_unit.getText(), question_unit['href']])

        question_name = question_unit.getText()
        question_link = parse_question_link(question_unit['href'])
        question_dict.append({"name":question_name, "link":question_link})

    return  question_dict

    # movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

def parse_question_link(link):
    obj = link.replace(r'\"http://link.zhihu.com/?target=https%3A//','').replace(r'\"','')
    obj_link = r"http://" + obj
    return obj_link



def main():
    url = DOWNLOAD_URL
    # while url:
    #     html = download_page(url)
    #     parse_html(html)
        
    with codecs.open('movies3', 'wb', encoding='utf-8') as fp:
    
        html = download_page(url)
        questions = parse_html(html)

        i=0
        for question_union in questions:
            i=i+1
            # name = question_union['name']
            # link = question_union['link']
            
            if i<5:
                str = u'{name}\n{link}\n'.format(name=question_union['name'], link=question_union['link'])
                fp.write(str)
                filename = question_union['name'] + '.pdf'
                pdfkit.from_url(question_union['link'], filename)

    print("OK")
        # fp.write(u'{movies}\n\n\n'.format(movies='\n'.join(movies)))
        # fp.write(u'{links}\n\n\n'.format(links='\n'.join(links)))

    # with codecs.open('movies3', 'wb', encoding='utf-8') as fp:
    #     while url:
    #         html = download_page(url)
    #         movies, url = parse_html(html)
    #         fp.write(u'{movies}\n\n\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()