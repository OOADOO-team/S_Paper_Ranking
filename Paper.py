class Paper:
    def __init__(self, title='', authors='', public_in='', data='', url='',
                 abstract='', citations=None, references=None):
        self.title = title
        self.authors = authors
        self.public_in = public_in
        self.data = data
        self.url = url
        self.abstract = abstract
        self.citations = citations
        self.references = references
        if citations is not None:
            self.num_citations = len(citations)
        else:
            self.num_citations = 0

    def add_references(self, new_paper):
        if self.references is not None:
            self.references.append(new_paper)
        else:
            self.references = []
            self.references.append(new_paper)

    def add_citations(self, new_paper):
        if self.citations is not None:
            self.citations.append(new_paper)
            self.num_citations += 1
        else:
            self.citations = []
            self.num_citations = 0

    def set_title(self, title):
        self.title = title

    def set_authors(self, authors):
        self.authors = authors

    def add_authors(self, authors):
        if self.authors == '':
            self.authors = authors
        else:
            self.authors += ',' + authors

    def set_public_in(self, public_in):
        self.public_in = public_in

    def set_data(self, data):
        self.data = data

    def set_url(self, data):
        self.url = url

    def set_abstract(self, abstract):
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

    def get_authors(self):
        return self.authors

    def get_public_in(self):
        return self.public_in

    def get_data(self):
        return self.data

    def get_url(self):
        return self.url

    def get_abstract(self, upper=False):
        if upper:
            return str.upper(self.abstract)
        return self.abstract

    def get_num_citations(self):
        return self.num_citations

    def get_references(self):
        return self.references

    def get_citations(self):
        return self.citations
