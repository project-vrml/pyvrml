import requests


def login(userName: str, password: str, loginUrl: str, redirectUrl: str):
    """
    通过登录进行验权，然后跳转到目标页面
    :param userName: 用户名
    :param password: 密码
    :param loginUrl: 登录链接
    :param redirectUrl: 跳转链接
    :return:
    """
    data = {
        "userName": userName,
        "password": password,
        "cn": "cn1",
        "keepAlive": True,
        "redirectUrl": redirectUrl
    }
    try:
        res = requests \
            .post(url=loginUrl,
                  data=data,
                  headers={'Content-Type': 'application/x-www-form-urlencoded'},
                  verify=False)
        return res
    except Exception as e:
        print('[login.login] error', e)
        return None
