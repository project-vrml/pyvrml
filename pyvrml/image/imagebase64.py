import base64
from io import BytesIO


def read_plt_to_base64_image(plt_obj, image_format='png'):
    """
    将plt绘图对象转为base64格式字符串
    :param image_format: 默认png格式
    :param plt_obj: plt
    :return: image
    """
    # 写入内存
    save_file = BytesIO()
    plt_obj.savefig(save_file, format=image_format)
    # 转换base64并以utf8格式输出
    save_file_base64 = base64.b64encode(save_file.getvalue()) \
        .decode('utf8')
    print(save_file_base64)
    return save_file_base64
