import csv


def read_csv(file_name):
    """
    读取CSV文件
    :param file_name: 文件路径名
    :return: 行列表
    """
    with open(file_name, 'r', encoding='UTF-8') as f:
        file = csv.reader(f)
        for line in file:
            yield line
