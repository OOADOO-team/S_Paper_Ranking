from read_database import get_refer_and_cita


class PaperBean:
    def __init__(self, number=0, title='', authors='', published_in='', url='',
                 abstract='', citations=[], references=[]):
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
        # paper的citation的list
        self._citations = citations
        # paper的reference的list
        self._references = references
        # paper的citation数目
        self._num_citations = 0

    @property
    def number(self):
        return int(self._number)

    @property
    def num_citations(self):
        """
        set时存的是 目前获取的该paper最大的citation number
        get时放的是 citation list的长度 和 number of citation 中的最大值
        """
        return max(len(self._citations), self._num_citations)

    @num_citations.setter
    def num_citations(self, num):
        if self._num_citations < num:
            self._num_citations = num

    @property
    def title(self):
        return str(self._title)

    @title.setter
    def title(self,name):
        self._title = name

    @property
    def authors(self):
        return str(self._authors)

    @authors.setter
    def authors(self, authors):
        self._authors = authors

    @property
    def references(self):
        """
        set时存的是 references number 的 list
        get时放的是 根据 references number 的 list 获取到的 paper的 list
        """
        if len(self._references) != 0:
            return get_refer_and_cita(self._references)
        else:
            return None

    @references.setter
    def references(self, references):
        self._references = references

    @property
    def citations(self):
        """
        set时存的是 citation number 的 list
        get时放的是 根据 citation number 的 list 获取到的 paper的 list
        """
        if len(self._citations) != 0:
            print(self._citations)
            return get_refer_and_cita(self._citations)
        else:
            return None

    @citations.setter
    def citations(self, citations):
        self._citations = citations

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

# ========================== method ===================================

    def search(self, keywords):
        title = str.upper(self.title)
        abstract = str.upper(self.abstract)
        try:
            keywords = str.upper(keywords)
        except TypeError as e:
            print(e)
            return False
        if keywords in title or keywords in abstract:
            return True
        return False

    def add_authors(self, authors):
        if self.authors == '':
            self._authors = authors
        else:
            self._authors += ',' + authors

    def add_references(self, new_paper_num):
        self.references.append(new_paper_num)

    def add_citations(self, new_paper_num):
        self.citations.append(new_paper_num)

