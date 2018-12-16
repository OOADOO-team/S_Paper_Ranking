class PaperBean:
    def __init__(self, title='', authors='', public_in='', data='', url='',
                 abstract='', citations=[], references=[]):
        self._title = title
        self._authors = authors
        self._public_in = public_in
        self._data = data
        self._url = url
        self._abstract = abstract
        self._citations = citations
        self._references = references
        self._num_citations = 0

    def add_references(self, new_paper):
        self.references.append(new_paper)

    def add_citations(self, new_paper):
        self.citations.append(new_paper)

    @property
    def num_citations(self):
        return max(len(self._citations), self._num_citations)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,name):
        self._title = name

    @property
    def authors(self):
        return str(self._authors)

    @property
    def references(self):
        return self._references

    @property
    def citations(self):
        return self._citations

    @property
    def public_in(self):
        return self._public_in

    @property
    def data(self):
        return self._data

    @property
    def url(self):
        return str(self._url)

    @property
    def abstract(self):
        return str(self._abstract)

    @authors.setter
    def authors(self, authors):
        self._authors = authors

    @url.setter
    def url(self, url):
        self._url = url

    @abstract.setter
    def abstract(self, abstract):
        self._abstract = abstract

    @citations.setter
    def citations(self, citations):
        self._citations = citations

    @num_citations.setter
    def num_citations(self, num):
        if self._num_citations < num:
            self._num_citations = num

    @references.setter
    def references(self,references):
        self._references = references

    @data.setter
    def data(self, data):
        self._data = data

    @public_in.setter
    def public_in(self, public_in):
        self._public_in = public_in

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

