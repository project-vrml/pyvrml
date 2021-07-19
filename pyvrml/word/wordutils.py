import os

# python-docx
from docx import Document


def search_str_in_paragraph(str_to_search, paragraph):
    """
    本函数旨在特定段落中搜索指定字符串，并返回字符串索引位置。
    """
    str_index = paragraph.text.index(str_to_search)

    return str_index


def read_path(path: str, search_text: str, file_name="docx", text_range=10):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            filename = file.split(".")[0]
            ext = file.split(".")[1]
            if ext == file_name:
                path_value = os.path.join(root, file)
                doc = Document(path_value)
                for paragraph in doc.paragraphs:
                    if search_text in paragraph.text:
                        str_index = search_str_in_paragraph(search_text, paragraph)
                        text_value = paragraph.text[str_index - text_range:str_index + text_range]
                        path_value = os.path.join(root, file)
                        print(text_value, "-----", filename, "-----", path_value)
