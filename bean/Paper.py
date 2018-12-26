class PaperBean:
    def __init__(self, number=0, title='', authors='', published_in='', url='',
                 abstract='', citations_name=[], references_name=[], citations_url=[],
                 reference_url=[], citation_number=0):
        # 记录paper的编号
        self._number = number
        # paper的名字
        self._title = title
        # paper的作者，可以有多个作者
        self._authors = authors
        # 出版社的名字
        self._published_in = published_in
        # paper对应的网址
        self._url = url
        # paper的简介
        self._abstract = abstract
        # paper的citation的list 里面存 name list
        self._citations_name = citations_name
        # paper的citation的list 里面存 url list
        self._citations_url = citations_url
        # paper的reference的list 里面存 name list
        self._references_name = references_name
        # paper的reference的list 里面存 url list
        self._references_url = reference_url
        # paper的citation数目
        self._citation_number = citation_number

    @property
    def number(self):
        return int(self._number)

    @number.setter
    def number(self, num):
        self._number = num

    @property
    def title(self):
        return str(self._title)

    @title.setter
    def title(self, name):
        self._title = name

    @property
    def authors(self):
        return str(self._authors)

    @authors.setter
    def authors(self, authors):
        self._authors = authors

    @property
    def published_in(self):
        return self._published_in

    @published_in.setter
    def published_in(self, publish_in):
        self._published_in = publish_in

    @property
    def url(self):
        return str(self._url)

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def abstract(self):
        return str(self._abstract)

    @abstract.setter
    def abstract(self, abstract):
        self._abstract = abstract

    @property
    def citations_name(self):
        if len(self._citations_name) != 0:
            # print(self._citations)
            return self._citations_name
        else:
            return None

    @citations_name.setter
    def citations_name(self, citations_name):
        self._citations_name = (citations_name)[1:-1].split("','")

    @property
    def citations_url(self):
        if len(self._citations_url) != 0:
            return self._citations_url
        else:
            return None

    @citations_url.setter
    def citations_url(self, citations_url):
        self._citations_url = citations_url

    @property
    def references_name(self):
        if len(self._references_name) != 0:
            return self._references_name
        else:
            return None

    @references_name.setter
    def references_name(self, references_name):
        self._references_name = str(references_name)[1:-1].split("','")

    @property
    def references_url(self):
        if len(self._references_url) != 0:
            return self._references_url
        else:
            return None

    @references_url.setter
    def references_url(self, references_url):
        self._references_url = references_url

    @property
    def citation_number(self):

        return max(int(self._citation_number), len(self.citations_name))

    @citation_number.setter
    def citation_number(self, cita_num):
        self._citation_number = int(cita_num)

