import csv

import pandas as pd


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


def write_csv(columns, data, file_name="data.csv"):
    """
    写入CSV文件
    :param columns: 列名列表
    :param data: 数据列表
    :param file_name: 文件路径名
    """
    file = pd.DataFrame(columns=columns, data=data)
    print(file)
    file.to_csv(file_name, encoding='gbk')
