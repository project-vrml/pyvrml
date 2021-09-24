import json

import requests

from pyvrml.utils.retryutils import http_retry_get, http_retry_get_json, http_retry_post_json


@http_retry_get
def get(url, params=None, headers=None):
    """
    带有重试功能的GET请求
    :param url: url
    :param params: a=a&b=b格式
    :return: JSON响应体
    """
    if params != None:
        url = url + "?" + params
    response = requests \
        .get(url=url,
             headers=headers,
             verify=False) \
        .json()
    return response


@http_retry_get_json
def get_json(url, params=None):
    """
    带有重试功能的GET请求
    :param url: url
    :param params: a=a&b=b格式
    :return: JSON响应体
    """
    if params != None:
        url = url + "?" + params
    response = requests \
        .get(url=url,
             headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
             verify=False) \
        .json()
    return response


@http_retry_post_json
def post_json(url, request):
    """
    带有重试功能的POST请求
    :param url: url
    :param request: JSON请求体
    :return: JSON响应体
    """
    response = requests \
        .post(url=url,
              headers={'Content-Type': 'application/json'},
              data=json.dumps(request)) \
        .json()
    return response
