import os

from docx import Document

from pyvrml.excel.excelutils import render_excel

path = input("请输入要搜索的路径(例如'D:\\Users\\shihaowang\\Projects\\Ten\\pyvrml\\demo\\search_word'):")

str_to_search = input("请输入要搜索的字段:")



def gen_excel(content_rows: []):
    title_list = ["text", "filename", "path"]
    render_excel(title_list=title_list,
                 content_rows=content_rows,
                 excel_name="word_keyword_search.xls")


def search_str_in_paragraph(str_to_search, paragraph):
    """
    本函数旨在特定段落中搜索指定字符串，并返回字符串索引位置。
    """
    str_index = paragraph.text.index(str_to_search)

    return str_index


if __name__ == '__main__':
    content_rows = []

    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            filename = file.split(".")[0]
            ext = file.split(".")[1]
            if ext == "docx":
                doc = Document(os.path.join(root, file))
                for paragraph in doc.paragraphs:
                    if str_to_search in paragraph.text:
                        str_index = search_str_in_paragraph(str_to_search, paragraph)
                        text_value = paragraph.text[str_index - 10:str_index + 10]
                        path_value = os.path.join(root, file)
                        print(text_value, "-----", filename, "-----", path_value)
                        content_rows.append([text_value, filename, path_value])

    gen_excel(content_rows)
