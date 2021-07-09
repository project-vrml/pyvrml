from pyvrml.excel.excelutils import render_excel


def gen_excel_demo1():
    title_list = ["email", "locale"]

    email_prefix = "kevinten"
    email_suffix = "@test.com"
    locale = "zh-hk"

    content_rows = []
    for i in range(10000):
        email = email_prefix + str(i) + email_suffix

        content_row = []
        content_row.append(email)
        content_row.append(locale)

        content_rows.append(content_row)

    render_excel(title_list=title_list,
                 content_rows=content_rows,
                 excel_name="email_locale_excel.xls")


# 生成execl文件
if __name__ == '__main__':
    gen_excel_demo1()
