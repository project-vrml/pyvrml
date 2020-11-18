from pyvrml.excel.excelutils import render_excel
from pyvrml.file.csvutils import read_csv
from pyvrml.gitlab.gitlab import gitlab_auth


def gitlab():
    # 1. 设置gitlab访问地址(不传为默认值)
    git_url = "http://git.com/"
    # 2. 设置gitlab访问token(在gitlab中生成)
    git_token = "token"
    # 3. 登录到gitlab并获得操作句柄
    gl = gitlab_auth(git_url=git_url, git_token=git_token)
    # 4. 请参考gitlab模块使用说明 https://python-gitlab.readthedocs.io/en/stable/api-objects.html
    # 5. 获取project
    project_name = "test"
    projects = gl.projects.list(search=project_name)
    [print(project) for project in projects]


def csv():
    """
    11,21,31
    12,22,32
    ........
    xx,xx,xx
    """
    # 1. 读入csv文件为二维数组
    rows = read_csv('uids.csv')
    [[print(col) for col in row] for row in rows]


def excel():
    # 1. 设置标题
    title_list = ["1", "2", "3", "4"]
    # 2. 设置内容
    content_rows = [["row11", "row12", "row13", "row14"],
                    ["row21", "row22", "row23", "row24"]]
    # 3. 设置名称
    name = "test.xls"
    # 4. 渲染为Excel
    render_excel(title_list=title_list,
                 content_rows=content_rows,
                 excel_name=name)


if __name__ == '__main__':
    print("[pyvrml api docs]-----------------------")

    print("[pyvrml 数据源]-----------------------")

    # gitlab
    gitlab()

    # csv
    csv()

    print("[pyvrml 通知形式]-----------------------")

    # excel
    excel()
