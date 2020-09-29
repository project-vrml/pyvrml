import json

import requests

from ..retry.retryable import http_retry


@http_retry
def post(url, request):
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
