# 默认最大重试次数
import time

retry_max_count = 100
# 默认重试等待时间s
retry_wait_second = 0.5


def http_retry_get(http_func):
    """
    对HTTP调用进行重试装饰
    :param http_func: HTTP调用方法
    :return: HTTP响应结果
    """

    def wrapper(url, params, headers):
        i = 1
        while i <= retry_max_count:
            try:
                return http_func(url, params, headers)
            except Exception as e:
                print("[retryutils.http.get] utils count: " + str(i) + ", error: ", e)
                time.sleep(retry_wait_second)
            i += 1

    return wrapper


def http_retry_get_json(http_func):
    """
    对HTTP调用进行重试装饰
    :param http_func: HTTP调用方法
    :return: HTTP响应结果
    """

    def wrapper(url, params):
        i = 1
        while i <= retry_max_count:
            try:
                return http_func(url, params)
            except Exception as e:
                print("[retryutils.http.get_json] utils count: " + str(i) + ", error: ", e)
                time.sleep(retry_wait_second)
            i += 1

    return wrapper


def http_retry_post_json(http_func):
    """
    对HTTP调用进行重试装饰
    :param http_func: HTTP调用方法
    :return: HTTP响应结果
    """

    def wrapper(url, request):
        i = 1
        while i <= retry_max_count:
            try:
                return http_func(url, request)
            except Exception as e:
                print("[retryutils.http.post_json] utils count: " + str(i) + ", error: ", e)
                time.sleep(retry_wait_second)
            i += 1

    return wrapper
