import time


def get_local_timestamp(date_str='2000-01-01'):
    offset_in_seconds = 9 * 60 * 60
    return time.mktime(time.strptime(date_str, '%Y-%m-%d')) + offset_in_seconds
