import requests
import time
import re
from bean.Paper import *
import random

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
    '183.95.80.102:8080',
    '123.160.31.71:8080',
    '115.231.128.79:8080',
    '166.111.77.32:80',
    '43.240.138.31:8080',
    '218.201.98.196:3128'
]


def get_Google_scholar(keyword):
    start_time = time.time()
    for i in range(0, 1):
        url = 'https://scholar.google.com/scholar?start=' \
              + str(i * 10) + '&q=' + keyword + '&hl=zh-CN&as_sdt=1,5&as_vis = 1'
        header['User_Agent'] = random.choice(my_headers)
        html = requests.get(url, headers=header, ip=random.choice(proxy_list))

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
                file.write("url: "+temp[9:-1]+'\n')
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

        file = open("Google_scholar" + str(i) + ".txt", "w", encoding='utf-8')
        file.write(html.text)
        file.close()
        print('%.2f' % (time.time() - start_time))
        start_time = time.time()


def get_ieee():
    start_time = time.time()
    url = 'https://ieeexplore.ieee.org/document/8472985'
    html = requests.get(url, header)
    cookies = html.cookies
    url = url + '/references'
    html = requests.get(url, cookies=cookies)
    file = open("ieee.txt", "w", encoding='utf-8')
    file.write(html.text)
    file.close()
    print('%.2f' % (time.time() - start_time))


if __name__ == '__main__':
    keyword = 'carp'
    get_Google_scholar(keyword)
    # get_ieee()
