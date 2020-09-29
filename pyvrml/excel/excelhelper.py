import pandas as pd
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


def parse_excel_to_html(file_name):
    """
    解析EXCEL到HTML输出
    :param file_name: EXCEL路径文件名
    :return: HTML代码
    """
    xd = pd.ExcelFile(file_name)
    df = xd.parse()
    return df.to_html(header=True, index=False)
