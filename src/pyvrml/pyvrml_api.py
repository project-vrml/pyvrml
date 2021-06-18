from src.pyvrml.http.http_api import VrmlHttpApi


class PyVrml(object):

    @staticmethod
    def http_api(url: str):
        return VrmlHttpApi(url=url)
