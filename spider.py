# -*- coding: utf-8 -*-
import requests
import time
import re
from bean.Paper import *
import random
import os

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
}

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) "
    "AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 '
    'Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) "
    "Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36"
]

proxy_list = [
    '140.207.50.246:51426',
    '60.191.201.38:45461',
    '61.145.69.27:42380'
]


def get_prox():
    proxy = random.choice(proxy_list)
    proxies = {
        # 'https': 'https://' + proxy,
        'http': 'http://' + proxy,
    }
    return proxies


def get_Google_scholar(keyword):
    start_time = time.time()
    for i in range(0, 1):
        if i % 5 == 4:
            time.sleep(10)
        url = 'https://scholar.google.com/scholar?start=' \
              + str(i * 10) + '&q=' + keyword + '&hl=zh-CN&as_sdt=1,5&as_vis = 1'
        header['User_Agent'] = random.choice(my_headers)
        try:
            html = requests.get(url, headers=header, proxies=get_prox(), timeout=5)
            if html.text.find('人机验证'):
                print('你已经凉了！被Google墙了！')
                return
        except requests.exceptions.ConnectionError as e:
            print('Error: ', e.args)
            return

        pattern = re.compile(r'<div class="gs_ri">.*?</div></div></div>')
        m = re.findall(pattern, html.text)
        if i == 0:
            file = open("Name.txt", "w", encoding='utf-8')
        else:
            file = open("Name.txt", "a", encoding='utf-8')
        for item in m:
            url_pattern = re.compile(r'<a href=".*?"')
            paper_pattern = re.compile(r'data-clk=.*?</a>')
            author_pattern = re.compile(r'<div class="gs_a">.*?</div>')
            abstruct_pattern = re.compile(r'<div class="gs_rs">.*?</div>')
            num_cit_pattern = re.compile(r'>被引用次数：.*?</a>')

            net = re.search(url_pattern, item)
            temp = net.group()
            if net is not None:
                file.write("url: " + temp[9:-1] + '\n')
            net = re.search(paper_pattern, item)
            if net is not None:
                temp = net.group().split('">')[-1]
                temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
                file.write("name: " + temp[:-4] + '\n')

            net = re.search(author_pattern, item)
            if net is not None:
                temp = net.group()[18:-6]
                temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
                file.write("author: " + temp + '\n')

            net = re.search(abstruct_pattern, item)
            if net is not None:
                temp = net.group()
                temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
                file.write("abstruct: " + temp[19:-6] + '\n')

            net = re.search(num_cit_pattern, item)
            if net is not None:
                temp = net.group()
                file.write(temp[1:-4] + '\n')

            file.write('\n')

        file.close()

        file = open("Google_scholar_" + str(i) + ".txt", "w", encoding='utf-8')
        file.write(html.text)
        file.close()
        print('%.2f' % (time.time() - start_time))
        start_time = time.time()


def get_doc_ieee(doc_link):
    header['User_Agent'] = random.choice(my_headers)
    start_time = time.time()
    doc = doc_link[10:-1]
    url = 'https://ieeexplore.ieee.org' + doc_link
    html = requests.get(url, header)
    cookies = html.cookies

    url = 'https://ieeexplore.ieee.org/rest' + doc_link + 'references'
    html = requests.get(url, header, cookies=cookies)
    if html is not None:
        file = open(doc + "_ref.txt", "w", encoding='utf-8')
        info = re.compile(r'{"order":.*?","context":')
        m = re.findall(info, html.text)
        for item in m:
            name_pattern = re.compile(r'title":".*?",')
            name = re.search(name_pattern, item)
            try:
                temp = name.group()[8:-2]
                if temp.endswith(','):
                    temp = temp[:-1]
                file.write(temp + '\r')
            except AttributeError as e:
                file.write('\r' + html.text)
                file.close()
                print(e.args)
                exit(0)
        file.close()

    url = url.replace('references', 'citations')
    html = requests.get(url, header, cookies=cookies)
    if html is not None:
        file = open(doc + "_cit.txt", "w", encoding='utf-8')
        info = re.compile(r'{"order":.*?","links":')
        m = re.findall(info, html.text)
        for item in m:
            name_pattern = re.compile(r'\\".*?\\"')
            name = re.search(name_pattern, item)
            if name is None:
                book_pattern = re.compile(r'<i>.*?</i>')
                name = re.search(book_pattern, item)
            try:
                temp = name.group()[2:-2]
                if temp.endswith('<'):
                    temp = temp[1:-2]
                file.write(temp + '\r')
            except AttributeError as e:
                file.write('\r' + html.text)
                file.close()
                print(e.args)
                exit(0)
        file.close()

    url = 'https://ieeexplore.ieee.org' + doc_link + 'authors'
    html = requests.get(url, header, cookies=cookies)
    if html is not None:
        file = open(doc + "_authors.txt", "w", encoding='utf-8')
        info = re.compile(r'"name":".*?","affiliation"')
        m = re.findall(info, html.text)
        for item in m:
            temp = item[8:-15]
            file.write(temp + '\r')
        file.close()

    print('%.2f' % (time.time() - start_time))


def get_ieee_search(keyword):
    header['User_Agent'] = random.choice(my_headers)
    start_time = time.time()
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=' + keyword
    html = requests.get(url, header)
    cookies = html.cookies
    header['Content-Type'] = 'application/json'
    url = 'https://ieeexplore.ieee.org/rest/search'
    for i in range(0, 1):
        if i == 0:
            data = '{"newsearch":true,' \
                   '"queryText":"' \
                   + keyword + \
                   '","highlight":true,' \
                   '"returnFacets":["ALL"],"' \
                   'returnType":"SEARCH"}'
        else:
            if i % 5 == 0:
                time.sleep(10)
            data = '{"newsearch":true,' \
                   '"queryText":"' \
                   + keyword + \
                   '","highlight":true,' \
                   '"returnFacets":["ALL"],' \
                   '"returnType":"SEARCH"' \
                   '"pageNumber":' + str(i + 1) + '}'
        info = re.compile(r'"articleTitle":.*?","publicationLink":.*?punumber=.*?"')
        html = requests.post(url, data, cookies=cookies, headers=header)
        m = re.findall(info, html.text)
        if i == 0:
            file = open(keyword + ".txt", "w", encoding='utf-8')
        else:
            file = open(keyword + ".txt", "a", encoding='utf-8')
        for item in m:
            name_pattern = re.compile(r'tle":".*?","pub')
            id_pattern = re.compile(r'punumber=.*?"')
            name = re.search(name_pattern, item).group()[6:-7]
            id = re.search(id_pattern, item).group().replace('punumber=', '')
            if id.endswith('"'):
                id = id[:-1]
            file.write(name.replace(' ', '_') + ' ' + id + '\r')
        file.close()

    del header['Content-Type']
    print('%.2f' % (time.time() - start_time))


def search_paper(keyword):
    paper_list = []

    get_ieee_search(keyword)
    file = open(keyword + '.txt', "r", encoding='utf-8')
    for line in file:
        name = line.split(' ')[0].replace('_', ' ')
        id = line.split(' ')[1][:-1]
        temp = PaperBean(title=name)
        time.sleep(5)
        get_doc_ieee('/document/'+ id + '/')

        file2 = open(id + '_ref.txt', "r", encoding='utf-8')
        for l in file2:
            temp.add_references(PaperBean(title=l[:-1]))
        file2.close()
        os.remove(id + '_ref.txt')

        file2 = open(id + '_cit.txt', "r", encoding='utf-8')
        for l in file2:
            temp.add_citations(PaperBean(title=l[:-1]))
        file2.close()
        os.remove(id + '_cit.txt')

        file2 = open(id + '_authors.txt', "r", encoding='utf-8')
        for l in file2:
            temp.add_authors(l[:-1])
        file2.close()
        os.remove(id + '_authors.txt')
    file.close()
    os.remove(keyword + '.txt')

    get_Baidu_scholar(keyword)
    file = open(keyword + '.txt', "r", encoding='utf-8')
    for line in file:
        name = line.replace(' ', '_').replace(':', '-')[:-1]
        file2 = open(name + '.txt', 'r', encoding='utf-8')
        l = file2.readlines()
        temp = PaperBean(title=l[0])
        temp.add_authors(l[1][:-2])
        temp.abstract = l[2][:-1]
        temp.data = l[3][:-1]
        file2.close()
        os.remove(name + '.txt')
    file.close()
    os.remove(keyword + '.txt')
    return paper_list


def get_Baidu_scholar(keyword):
    start_time = time.time()
    class_pattern = re.compile(r'<h3 class="t c_font">[\s\S]*?</a>')
    url_pattern = re.compile(r'href=".*?"')
    id_pattern = re.compile(r'data-longsign=".*?"')
    body_pattern = re.compile(r'<a href=".*?data-click=.*?\'title\'}" target=.*?</a>')
    name_pattern = re.compile(r'">.*?</a>')
    author_pattern = re.compile(r'<span><a href=.*?author.*?</a></span>')
    author_name_pattern = re.compile(r'">.*?</a></span>')
    abstract_pattern = re.compile(r'<p class="abstract".*?</p>')
    ref_pattern = re.compile(r'<p class="ref-wr-num".*?</a>', re.DOTALL)
    num_pattern = re.compile(r'[\s]+?[\d]+', re.DOTALL)
    for i in range(0, 1):
        if i != 0:
            time.sleep(10)
        header['User_Agent'] = random.choice(my_headers)
        url = 'http://xueshu.baidu.com/s?wd=' + keyword.replace(' ', '%20') + '&pn=' + str(i * 10) + \
              '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1 '
        try:
            html = requests.get(url, headers=header, timeout=5)
        except requests.exceptions.ConnectionError as e:
            print('Error: ', e.args)
            return
        if i == 0:
            file = open(keyword + '.txt', "w", encoding='utf-8')
        else:
            file = open(keyword + '.txt', "a", encoding='utf-8')
        m = re.findall(class_pattern, html.text)
        cookie = html.cookies
        new_url = ''
        temp = html.text
        try:
            for item in m:
                new_url = re.search(url_pattern, item).group()[6:-1]
                new_url = 'http://xueshu.baidu.com' + new_url
                html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                id = re.search(id_pattern, html.text).group().replace('data-longsign="', '')[:-1]
                new_url = 'http://xueshu.baidu.com/usercenter/paper/show?paperid=' \
                          + id + '&site=xueshu_se'
                html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                body = re.search(body_pattern, html.text).group()
                name = re.search(name_pattern, body).group()[2:-4]
                file2 = open(name.replace(' ', '_').replace(':', "-") + '.txt', "w", encoding='utf-8')
                file2.write(name + '\r')
                file.write(name + '\r')
                authors = re.findall(author_pattern, html.text)
                for author in authors:
                    it = re.search(author_name_pattern, author).group()
                    file2.write(it[2:-11] + ',')
                file2.write('\r')
                abstract = re.search(abstract_pattern, html.text).group()
                abstract = abstract[abstract.find('>') + 1:-4]
                abstract.replace('</p>', '')
                file2.write(abstract + '\r')
                ref_num = re.search(ref_pattern, html.text).group()
                number = re.search(num_pattern, ref_num).group()
                number = re.search("\d+", number).group()
                file2.write(number + '\r')
                file2.close()
        except AttributeError as e:
            file.write(new_url + '\r')
            print(e)
        file.close()
    print('%.2f' % (time.time() - start_time))


if __name__ == '__main__':
    # get_Google_scholar('Anomaly Detection')
    for i in search_paper('Anomaly Detection'):
        print(i.title)
        print(i.authors)
        print('')
