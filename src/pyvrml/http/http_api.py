import requests


class VrmlHttpApi(object):
    """
    Vrml Http Api
    :param url: url
    :param verify: verify
    """
    url: str
    verify: bool

    def __init__(self, url: str):
        self.url = url
        self.verify = False

    def __init__(self, url: str, verify: bool):
        self.url = url
        self.verify = verify

    def get(self) -> object:
        return requests \
            .get(url=self.url) \
            .json()

    def get(self, params: str) -> object:
        _url = self.url + "?" + params
        return requests \
            .get(url=_url) \
            .json()

    def get(self, headers: dict) -> object:
        return requests \
            .get(url=self.url,
                 headers=headers) \
            .json()

    def get(self, headers: dict, params: str) -> object:
        _url = self.url + "?" + params
        return requests \
            .get(url=_url,
                 headers=headers) \
            .json()


class VrmlJsonHttpApi(VrmlHttpApi):
    headers: dict

    def __init__(self, url: str):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.verify = False

    def __init__(self, url: str, verify: bool):
        self.url = url
        self.verify = verify
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def __init__(self, url: str, headers: dict):
        self.url = url
        self.headers = headers
        self.verify = False

    def __init__(self, url: str, headers: dict, verify: bool):
        self.url = url
        self.headers = headers
        self.verify = verify
