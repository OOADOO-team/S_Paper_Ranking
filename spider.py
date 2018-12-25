# -*- coding: utf-8 -*-
import requests
import time
import re
import random
import os

'''
生成以 Paper名为名的 txt 格式文件， 文件内容如下：( _ 均表示有空格
name:_
url:_
public_in:_
authors:_
abstract:_
citations_number:_ 注：本条目可能缺省
Citation:_  注：数目不大于citations_number，但citations_number缺省时仍有可能存在
citation1文章名_"作者"_文章链接
citation2文章名_"作者"_文章链接 
...
References:_
reference1文章名_"作者"_文章链接
reference2文章名_"作者"_文章链接
...

'''

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, application/json, */*',
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
    '116.62.134.173:9999',
    # '111.177.168.240:3128',
    # '119.101.116.195:9999',
    # '114.112.70.150:43887',
    # '47.104.74.174:8118',
    # '121.232.148.82:9000'
]

N = 30  # 爬取搜索结果页数，注意，提高页数有可能导致被墙= =


def get_proxies():
    proxy = random.choice(proxy_list)
    proxies = {
        # 'https': 'https://' + proxy,
        'http': 'http://' + proxy,
    }
    return proxies


# def get_Google_scholar(keyword):
#     start_time = time.time()
#     for i in range(0, 1):
#         if i % 5 == 4:
#             time.sleep(10)
#         url = 'https://scholar.google.com/scholar?start=' \
#               + str(i * 10) + '&q=' + keyword + '&hl=zh-CN&as_sdt=1,5&as_vis = 1'
#         header['User_Agent'] = random.choice(my_headers)
#         try:
#             html = requests.get(url, headers=header, proxies=get_prox(), timeout=5)
#             if html.text.find('人机验证'):
#                 print('你已经凉了！被Google墙了！')
#                 return
#         except requests.exceptions.ConnectionError as e:
#             print('Error: ', e.args)
#             return
#
#         pattern = re.compile(r'<div class="gs_ri">.*?</div></div></div>')
#         m = re.findall(pattern, html.text)
#         if i == 0:
#             file = open("Name.txt", "w", encoding='utf-8')
#         else:
#             file = open("Name.txt", "a", encoding='utf-8')
#         for item in m:
#             url_pattern = re.compile(r'<a href=".*?"')
#             paper_pattern = re.compile(r'data-clk=.*?</a>')
#             author_pattern = re.compile(r'<div class="gs_a">.*?</div>')
#             abstruct_pattern = re.compile(r'<div class="gs_rs">.*?</div>')
#             num_cit_pattern = re.compile(r'>被引用次数：.*?</a>')
#
#             net = re.search(url_pattern, item)
#             temp = net.group()
#             if net is not None:
#                 file.write("url: " + temp[9:-1] + '\n')
#             net = re.search(paper_pattern, item)
#             if net is not None:
#                 temp = net.group().split('">')[-1]
#                 temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
#                 file.write("name: " + temp[:-4] + '\n')
#
#             net = re.search(author_pattern, item)
#             if net is not None:
#                 temp = net.group()[18:-6]
#                 temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
#                 file.write("author: " + temp + '\n')
#
#             net = re.search(abstruct_pattern, item)
#             if net is not None:
#                 temp = net.group()
#                 temp = temp.replace("<b>", " ").replace("<br>", " ").replace("</b>", " ")
#                 file.write("abstruct: " + temp[19:-6] + '\n')
#
#             net = re.search(num_cit_pattern, item)
#             if net is not None:
#                 temp = net.group()
#                 file.write(temp[1:-4] + '\n')
#
#             file.write('\n')
#
#         file.close()
#
#         file = open("Google_scholar_" + str(i) + ".txt", "w", encoding='utf-8')
#         file.write(html.text)
#         file.close()
#         print('%.2f' % (time.time() - start_time))
#         start_time = time.time()


def get_doc_ieee(doc_name, doc_link):
    
    header['User_Agent'] = random.choice(my_headers)
    start_time = time.time()
    url = 'https://ieeexplore.ieee.org' + doc_link
    html = requests.get(url, header, timeout=5)
    cookies = html.cookies
    file_name = re.sub(r'[/:*?"<>|]', '-', doc_name)
    if file_name.find('//') != -1:
        file_name = file_name.replace('//', ' ')
    url_pattern = re.compile(r'pdfUrl":".*?"')
    publication_pattern = re.compile(r'"publicationTitle":".*?"')
    abstract_pattern = re.compile(r'[^{]"abstract":".*?\."')
    if os.path.exists(file_name + '.txt'):
        return
    if len(file_name) > 150:
        file_name = file_name[:150]
    if os.path.exists(file_name + '.txt'):
        return
    file = open(file_name + '.txt', 'w', encoding='utf-8')
    try:
        file.write('name: ' + doc_name + '\r')
        try:
            paper_url = re.search(url_pattern, html.text).group()[9:-1]
            paper_url = 'https://ieeexplore.ieee.org' + paper_url
        except AttributeError:
            file.close()
            os.remove(file_name + '.txt')
            return
        file.write('url: ' + paper_url + '\r')
        publication = re.search(publication_pattern, html.text).group()[20:-1]
        file.write('public_in: ' + publication + '\r')

        file.write('authors: ')
        new_url = 'https://ieeexplore.ieee.org' + doc_link + 'authors'
        html2 = requests.get(new_url, header, cookies=cookies, timeout=5)
        if html2 is not None:
            info = re.compile(r'"name":".*?","affiliation"')
            m = re.findall(info, html2.text)
            for item in m:
                temp = item[8:-15]
                file.write(temp + ',')
        file.write('\r')

        abstract = re.search(abstract_pattern, html.text)
        if abstract is not None:
            abstract = abstract.group()[13:-1]
        else:
            abstract = ''

        file.write('abstract: ' + abstract + '\r')
    except AttributeError:
        file.close()
        file = open('Error.txt', 'w', encoding='utf-8')
        file.write(html.text)
        exit(0)

    url = 'https://ieeexplore.ieee.org/rest' + doc_link + 'citations'
    html = requests.get(url, header, cookies=cookies, timeout=5)
    file.write('Citations: \r')
    if html is not None:
        info = re.compile(r'{"order":.*?title":".*?"}')
        name_pattern = re.compile(r'title":".*?"')
        doi_pattern = re.compile(r'"crossRefLink":".*?"')
        ref_url_pattern = re.compile(r'"pdfLink":".*?"')
        google_pattern = re.compile(r'"googleScholarLink":".*?"')
        ref_author_pattern = re.compile(r'ext":".*?"')
        m = re.findall(info, html.text)
        for item in m:
            if item.find('[online]') != -1:
                continue
            try:
                name = re.search(name_pattern, item).group()[8:-2]
                if name.endswith(','):
                    name = name[:-1]
                file.write(name + ' ')
            except AttributeError:
                continue
            ref_authors = re.search(ref_author_pattern, item).group()[6:-2]
            ref_authors = ref_authors.split(',')
            for ref_aut in ref_authors:
                if ref_aut != '':
                    file.write('"' + ref_aut + '"')
            doi = re.search(doi_pattern, item)
            if doi is not None:
                doi = doi.group()[16:-1]
                file.write(doi + '\r')
                continue
            pdf = re.search(ref_url_pattern, item)
            if pdf is not None:
                pdf = pdf.group()[11:-1]
                file.write('https://ieeexplore.ieee.org' + pdf + '\r')
                continue
            google_url = re.search(google_pattern, item)
            if google_url is not None:
                google_url = google_url.group()[21:-1]
                file.write(google_url + '\r')
                continue
            file.write('\r')

    file.write('References: \r')
    url = 'https://ieeexplore.ieee.org/rest' + doc_link + 'references'
    html = requests.get(url, header, cookies=cookies, timeout=5)
    print(url)
    if html is not None:
        info = re.compile(r'{"order":.*?id":"ref.*?"}')
        name_pattern = re.compile(r'title":".*?",')
        doi_pattern = re.compile(r'"crossRefLink":".*?"')
        ref_url_pattern = re.compile(r'"pdfLink":".*?"')
        google_pattern = re.compile(r'"googleScholarLink":".*?"')
        ref_author_pattern = re.compile(r'ext":".*?"')
        m = re.findall(info, html.text)
        for item in m:
            if item.find('[online]') != -1:
                continue
            try:
                name = re.search(name_pattern, item).group()[8:-2]
                if name.endswith(','):
                    name = name[:-1]
                file.write(name + ' ')
            except AttributeError:
                continue
            ref_authors = re.search(ref_author_pattern, item).group()[6:-2]
            ref_authors = ref_authors.split(',')
            for ref_aut in ref_authors:
                if ref_aut != '':
                    file.write('"' + ref_aut + '"')
            doi = re.search(doi_pattern, item)
            if doi is not None:
                doi = doi.group()[16:-1]
                file.write(doi + '\r')
                continue
            pdf = re.search(ref_url_pattern, item)
            if pdf is not None:
                pdf = pdf.group()[11:-1]
                file.write(pdf + '\r')
                continue
            google_url = re.search(google_pattern, item)
            if google_url is not None:
                google_url = google_url.group()[21:-1]
                file.write(google_url + '\r')
                continue
            file.write('\r')
    file.close()

    print('%.2f' % (time.time() - start_time))


def get_ieee_search(keyword):
    header['User_Agent'] = random.choice(my_headers)
    
    start_time = time.time()
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=' + keyword
    html = requests.get(url, header, timeout=5)
    cookies = html.cookies
    header['Content-Type'] = 'application/json'
    url = 'https://ieeexplore.ieee.org/rest/search'
    for i in range(0, N):
        if i == 0:
            data = '{"newsearch":true,' \
                   '"queryText":"' \
                   + keyword + \
                   '","highlight":true,' \
                   '"returnFacets":["ALL"],"' \
                   'returnType":"SEARCH"}'
        else:
            time.sleep(10)
            data = '{"newsearch":true,' \
                   '"queryText":"' \
                   + keyword + \
                   '","highlight":true,' \
                   '"returnFacets":["ALL"],' \
                   '"returnType":"SEARCH",' \
                   '"pageNumber":' + str(i + 1) + '}'
        info = re.compile(r'documentLink":".*?"articleTitle":".*?"')
        html = requests.post(url, data, cookies=cookies, headers=header, timeout=5)
        cookies = html.cookies
        m = re.findall(info, html.text)
        if html.text == '':
            print('error')
            exit(0)
        # file = open('temp.txt', 'w', encoding='utf-8')
        # file.write(html.text)
        # file.write(data)
        # file.close()
        # exit(0)

        for item in m:
            name_pattern = re.compile(r'"articleTitle":".*?"')
            id_pattern = re.compile(r'documentLink":".*?"')
            name = re.search(name_pattern, item).group()[16:-1]
            id = re.search(id_pattern, item).group().replace('documentLink":"/document/', '')
            if id.endswith('"'):
                id = id[:-2]
            print(name, id)
            try:
                get_doc_ieee(name, '/document/' + id + '/')
            except TimeoutError:
                pass

    del header['Content-Type']
    print('%.2f' % (time.time() - start_time))


def get_Baidu_scholar(keyword):
    class_pattern = re.compile(r'<h3 class="t c_font">[\s\S]*?</a>')
    url_pattern = re.compile(r'href=".*?"')
    id_pattern = re.compile(r'data-longsign=".*?"')
    body_pattern = re.compile(r'<a href=".*?data-click=.*?\'title\'}" target=.*?</a>')
    name_pattern = re.compile(r'">.*?</a>')
    paper_url_pattern = re.compile(r'http://.*?"')
    publication_pattern = re.compile(r'<a class="journal_title".*?</a>', re.DOTALL)
    author_pattern = re.compile(r'<span><a href=.*?author.*?</a></span>')
    author_name_pattern = re.compile(r'">.*?</a></span>')
    abstract_pattern = re.compile(r'<p class="abstract".*?</p>')
    ref_pattern = re.compile(r'<p class="ref-wr-num".*?</a>', re.DOTALL)
    num_pattern = re.compile(r'[\s]+?[\d]+', re.DOTALL)
    token_pattern = re.compile(r'bds.cf.token = ".*?";')
    ts_pattern = re.compile(r'bds.cf.ts = ".*?";')
    sign_pattern = re.compile(r'bds.cf.sign = ".*?";')
    paperid_pattern = re.compile(r'paperid: \'.*?\'')
    ref_body_pattern = re.compile(r'"sc_longsign":\[".*?"sc_title":\[".*?"\]')
    ref_name_pattern = re.compile(r'"sc_title":\[".*?"\]')
    ref_author_pattern = re.compile(r'sc_name":\[".*?"')
    ref_id_pattern = re.compile(r'"sc_longsign":\[".*?"\]')
    for i in range(0, N):
        start_time = time.time()
        
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
        if os.path.exists(keyword + '.txt'):
            file = open(keyword + '.txt', "a", encoding='utf-8')
        else:
            file = open(keyword + '.txt', "w", encoding='utf-8')
        m = re.findall(class_pattern, html.text)
        cookie = html.cookies
        new_url = ''
        for item in m:
            try:
                new_url = re.search(url_pattern, item).group()[6:-1]
                new_url = 'http://xueshu.baidu.com' + new_url
                html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                id = re.search(id_pattern, html.text)
                if id is None:
                    continue
                id = id.group().replace('data-longsign="', '')[:-1]
                if id == '':
                    continue
                new_url = 'http://xueshu.baidu.com/usercenter/paper/show?paperid=' \
                          + id + '&site=xueshu_se'
                html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                body = re.search(body_pattern, html.text).group()
                name = re.search(name_pattern, body).group()[2:-4]
                file_name = re.sub(r'[/:*?"<>|]', '-', name)
                if file_name.find('\\') != -1:
                    file_name = file_name.replace('\\', '')
                while file_name.find('[') != -1 and file_name.find(']') != -1:
                    file_name = file_name[:file_name.find('[')] + file_name[file_name.find(']')+1:]
                if os.path.exists(file_name + '.txt'):
                    continue
                if len(file_name) > 150:
                    file_name = file_name[:150]
                if os.path.exists(file_name + '.txt'):
                    continue
                file2 = open(file_name + '.txt', "w", encoding='utf-8')

                file2.write('name: ' + name + '\r')
                paper_url = re.search(paper_url_pattern, body).group()[:-1]
                file2.write('url: ' + paper_url + '\r')
                file.write(name + '\r')
                try:
                    publication = re.search(publication_pattern, html.text).group()
                    publication = re.search(name_pattern, publication).group()[2:-4]
                    file2.write('public_in: ' + publication + '\r')
                except AttributeError:
                    file2.write('public_in: None\r')
                authors = re.findall(author_pattern, html.text)
                file2.write('authors: ')
                for author in authors:
                    it = re.search(author_name_pattern, author).group()
                    file2.write(it[2:-11] + ',')
                file2.write('\r')
                try:
                    abstract = re.search(abstract_pattern, html.text).group()
                    abstract = abstract[abstract.find('>') + 1:-4]
                    abstract.replace('</p>', '')
                except AttributeError:
                    abstract = 'None'
                file2.write('abstract: ' + abstract + '\r')
                ref_num = re.search(ref_pattern, html.text).group()
                number = re.search(num_pattern, ref_num).group()
                number = re.search(r'\d+', number).group()
                file2.write('citations_number: ' + number + '\r')
                paperid = re.search(paperid_pattern, html.text).group()[10:-1]
                ts = re.search(ts_pattern, html.text).group()[13:-2]
                token = re.search(token_pattern, html.text).group()[16:-2]
                sign = re.search(sign_pattern, html.text).group()[15:-2]

                file2.write('Citation: \r')
                try:
                    new_url = 'http://xueshu.baidu.com/usercenter/paper/search?_token=' \
                              + token + '&_ts=' + ts + '&_sign=' + sign + '&wd=refpaperuri%3A(' \
                              + paperid + ')&type=citation&rn=10&page_no=1'
                    html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                    refbody = re.findall(ref_body_pattern, html.text)
                    for ref in refbody:
                        ref_id = re.search(ref_id_pattern, ref).group()[16:-2]
                        ref_name = re.search(ref_name_pattern, ref).group()[13:-2]
                        file2.write(ref_name + ' ')
                        ref_authors = re.findall(ref_author_pattern, ref)
                        for ref_aut in ref_authors:
                            if ref_aut.find(r'\u'):
                                ref_aut = ref_aut.encode().decode('unicode_escape')
                            file2.write(ref_aut[10:] + ' ')
                        file2.write('http://xueshu.baidu.com/usercenter/paper/show?paperid=' + ref_id + '\r')
                except requests.ReadTimeout:
                    print("cit timeout")
                    pass

                mark = 1
                first_ref = ''
                new_url_src = 'http://xueshu.baidu.com/usercenter/paper/search?_token=' \
                          + token + '&_ts=' + ts + '&_sign=' + sign + '&wd=citepaperuri%3A(' \
                          + paperid + ')&type=reference&rn=10&page_no='
                file2.write('References: \r')
                try:
                    while True:
                        new_url = new_url_src + str(mark)
                        mark += 1
                        num = 0
                        html = requests.get(new_url, headers=header, timeout=5, cookies=cookie)
                        refbody = re.findall(ref_body_pattern, html.text)
                        for ref in refbody:
                            ref_id = re.search(ref_id_pattern, ref).group()[16:-2]
                            if num == 0:
                                if first_ref == ref_id:
                                    break
                                else:
                                    first_ref = ref_id
                            num += 1
                            ref_name = re.search(ref_name_pattern, ref).group()[13:-2]
                            file2.write(ref_name + ' ')
                            ref_authors = re.findall(ref_author_pattern, ref)
                            for ref_aut in ref_authors:
                                if ref_aut.find(r'\u'):
                                    ref_aut = ref_aut.encode().decode('unicode_escape')
                                if ref_aut.find('全网免费下载') >= 0:
                                    continue
                                file2.write(ref_aut[10:] + ' ')
                            file2.write('http://xueshu.baidu.com/usercenter/paper/show?paperid=' + ref_id + '\r')
                        if num < 10:
                            break
                except requests.ReadTimeout:
                    print("ref timeout")
                    pass
                file2.close()
            except AttributeError as e:
                print(new_url)
                print(url)
                file2.close()
                os.remove(file_name + '.txt')
                print(e.args)
            except requests.ReadTimeout as e:
                print(new_url)
                print(url)
                file2.close()
                os.remove(file_name + '.txt')
                print(e.args)
        file.close()
        os.remove(keyword + '.txt')
        print('%.2f' % (time.time() - start_time))


if __name__ == '__main__':
    # get_Google_scholar('Anomaly Detection')   谷歌没写好
    # get_ieee_search('network')
    get_Baidu_scholar('A Machine-Learning Approach')
