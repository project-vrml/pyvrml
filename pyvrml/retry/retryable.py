# 默认最大重试次数
import time

# 默认执行10次重试
retry_max_count = 10


def http_retry(http_func):
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
                print("[retry.http] retry count: " + str(i) + ", error: ", e)
                time.sleep(0.1)
            i += 1

    return wrapper


def login_retry(http_func):
    """
    对LOGIN调用进行重试装饰
    :param http_func: LOGIN调用方法
    :return: LOGIN响应结果
    """

    def wrapper(userName, password, loginUrl, redirectUrl):
        i = 1
        while i <= retry_max_count:
            try:
                return http_func(userName, password, loginUrl, redirectUrl)
            except Exception as e:
                print("[retry.login] retry count: " + str(i) + ", error: ", e)
                time.sleep(0.1)
            i += 1

    return wrapper
