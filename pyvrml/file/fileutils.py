import os


def remove_file(file_name):
    """
    删除文件
    :param file_name: 路径文件名
    """
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('[fileutils.remove] no such file:%s' % file_name)
