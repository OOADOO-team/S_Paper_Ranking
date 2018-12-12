import requests
import time
import re
from bean.Paper import *

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
}


def get_Google_scholar(keyword):
    start_time = time.time()
    for i in range(0, 1):
        url = 'https://scholar.google.com/scholar?start=' \
              + str(i * 10) + '&q=' + keyword + '&hl=zh-CN&as_sdt=1,5&as_vis = 1'
        html = requests.get(url, headers=header)

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
