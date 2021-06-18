import requests


class VrmlHttpApi(object):
    """
    Vrml Http Api
    """
    url: str

    def __init__(self, url: str):
        self.url = url

    def get(self) -> object:
        return requests.get(url=self.url).json()
