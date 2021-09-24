import json

import requests
import xlwt


def render_excel(title_list: [], content_rows: [[]], excel_name='excel.xls'):
    """
    生成EXCEL报表
    :param title_list: 标题
    :param content_rows: 内容
    :param excel_name: 文件名称
    """
    w = xlwt.Workbook(encoding='ascii')  # 创建一个工作簿
    ws = w.add_sheet('1')  # 创建一个工作表

    # 标题
    for j in range(0, len(title_list)):
        ws.write(0, j, title_list[j])

    # 行
    for i in range(0, len(content_rows)):
        content_row = content_rows[i]
        # 列
        for j in range(0, len(content_row)):
            ws.write(i + 1, j, content_row[j])

    w.save(excel_name)


def get_data():
    url = ''
    request = {
    }

    response = requests \
        .post(url=url,
              headers={'Content-Type': 'application/json'},
              data=json.dumps(request)) \
        .json()
    return response


def compare(request):
    origin = {
    }

    # todo 对比逻辑
    return [['new', '123'], ['origin', '345']]


if __name__ == '__main__':
    # 1. 获取接口数据
    response = get_data()

    # 2. 对比数据
    data = compare(response['data'])

    # 3. xuanranshuju
    render_excel(['name', 'id'], data)
