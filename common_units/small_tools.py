from datetime import datetime
import time


def get_time():
    return datetime.now()


def print_info(info):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + info)
