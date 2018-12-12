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


    def add_references(self, new_paper):
        self.references.append(new_paper)

    def add_citations(self, new_paper):
        self.citations.append(new_paper)

    @property
    def num_citations(self):
        return len(self._citations)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,name):
        self._title = name

    @property
    def authors(self):
        return str(self._authors)


    def add_authors(self, authors):
        if self.authors == '':
            self.authors = authors
        else:
            self.authors += ',' + authors

    def set_public_in(self, public_in):
        self.public_in = public_in



    @property
    def data(self):
        return self._data

    @data.setter
    def set_data(self, data):
        self.data = data
    @property
    def url(self):
        return str(self._url)

    @property
    def abstract(self):
        return str(self._abstract)

    @authors.setter
    def authors(self, authors):
        self.authors = authors

    @url.setter
    def url(self, url):
        self._url = url

    @abstract.setter
    def abstract(self, abstract):
        self.abstract = abstract

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

    def get_title(self, upper=False):
        if upper:
            return str.upper(self.title)
        return self.title

    def get_references(self):
        return self.references

    def get_citations(self):
        return self.citations
