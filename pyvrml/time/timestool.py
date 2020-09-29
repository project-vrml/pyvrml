import datetime
import time


def current_datetime():
    """
    (时间对象)当前日期+时间
    :return 2020-08-31 15:01:29.119824
    """
    return datetime.datetime.now()


def current_date_zero_time():
    """
    (时间对象)当前日期+0时间
    :return 2020-08-31 00:00:00
    """
    now = current_datetime()
    return now - datetime.timedelta(hours=now.hour,
                                    minutes=now.minute,
                                    seconds=now.second,
                                    microseconds=now.microsecond)


def _x_day_ago_datetime(base_datetime, x_days=1):
    """
    (时间对象)(当前日期-x天)+时间
    :return 2020-08-30 15:01:29.119824
    """
    return base_datetime - datetime.timedelta(days=x_days)


def _x_day_after_datetime(base_datetime, x_days=1):
    """
    (时间对象)(当前日期+x天)+时间
    :return 2020-09-01 15:01:29.119824
    """
    return base_datetime + datetime.timedelta(days=x_days)


def parse_str_datetime(str_datetime):
    """
    (时间对象)解析到日期时间
    :return: %Y-%m-%d %H:%M:%S
    """
    return datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")


def format_date_str(datetime):
    """
    (字符串)格式化到日期字符串
    :param datetime : timestamp
    :return: str(date)
    """
    return datetime.strftime('%Y-%m-%d')


def parse_datetime_to_timestamp(datetime):
    """
    (时间戳)解析到时间戳
    :param datetime: datetime
    :return: timestamp(ms)
    """
    time_array = time.strptime(str(datetime), "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array)) * 1000


def format_timestamp_to_datetime(timestamp):
    """
    (字符串)格式化到日期时间字符串
    :return: datetime
    """
    try:
        return datetime.datetime.fromtimestamp(timestamp / 1000, None)  # 时间戳转换成字符串日期时间
    except Exception as e:
        print(e)
        return ''


def format_timestamp_to_date_str(timestamp):
    """
    (字符串)格式化到日期字符串
    :return: str(%Y-%m-%d)
    """
    date_time = format_timestamp_to_datetime(timestamp)
    return date_time.strftime('%Y-%m-%d')


if __name__ == '__main__':
    print(current_datetime())
    print(current_date_zero_time())
    print(_x_day_ago_datetime(current_datetime()))
    print(_x_day_ago_datetime(current_date_zero_time()))
    print(parse_datetime_to_timestamp(current_datetime().strftime("%Y-%m-%d %H:%M:%S")))
    print(parse_str_datetime("2000-01-30 00:00:00"))
    print(format_date_str(current_date_zero_time()))
    print(format_timestamp_to_datetime(1598858361000))
    print(format_timestamp_to_date_str(1598858361000))
