import gitlab


def gitlab_auth(git_url: str, git_token: str):
    """
    登录到gitlab
    :return: gl操作柄
    """
    url = git_url  # gitlab服务端地址
    private_token = git_token  # 授权一个token
    gl = gitlab.Gitlab(url, private_token, api_version='4')  # api_version默认是4，具体看自己公司的版本
    gl.auth()  # 主动发起认证，好像不要也能获取到数据
    return gl
