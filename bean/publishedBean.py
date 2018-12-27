class publishedBean():
    def __init__(self, id=0, published_name="", IF_value=0):
        self._id = id
        self._published_name = published_name
        self._IF_value = IF_value

    @property
    def id(self):
        return int(self._id)

    @id.setter
    def id(self, id):
        self._id = int(id)

    @property
    def published_name(self):
        return self._published_name

    @published_name.setter
    def published_name(self,published_name):
        self._published_name = published_name

    @property
    def IF_value(self):
        return float(self._IF_value)

    @IF_value.setter
    def IF_value(self, IF_value):
        self._IF_value = float(IF_value)
