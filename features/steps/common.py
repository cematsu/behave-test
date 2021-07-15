from json import JSONEncoder


class RequestEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__