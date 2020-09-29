from pyvrml.excel.excelhelper import render_excel
from pyvrml.file.csvhelper import read_csv


def csv_to_excel_demo1():
    rows = read_csv('test1.csv')

    title_list = ["code", "scheme", "message", "name"]

    content_rows = []
    for row in rows:
        name = row[0].strip()
        code = row[1].strip()
        scheme = row[2].strip()
        message = row[3].strip()

        content_row = []
        content_row.append(code)
        content_row.append(scheme)
        content_row.append(message)
        content_row.append(name)

        content_rows.append(content_row)

    render_excel(title_list=title_list,
                 content_rows=content_rows,
                 excel_name="test1.xls")


def csv_to_excel_demo2():
    rows = read_csv('test2.csv')

    title_list = ["1", "2", "3"]

    content_rows = []
    for row in rows:

        content_row = []
        for col in row:
            content_row.append(str(col))

        content_rows.append(content_row)

    render_excel(title_list=title_list,
                 content_rows=content_rows,
                 excel_name="test2.xls")


if __name__ == '__main__':
    csv_to_excel_demo1()
    csv_to_excel_demo2()
