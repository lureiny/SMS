# -*- coding:utf-8 -*-

"""
从"*.ini"配置文件中获取配置信息
"""

from configparser import ConfigParser
import pathlib


def get_config_dict(config_name="config.ini"):
    config_dict = dict()
    config = ConfigParser()
    config_path = pathlib.PurePath(__file__).parent / config_name
    config.read(config_path)
    for section in config.keys():
        config_dict[section] = dict(config.items(section))
    return config_dict

 
class ConfigReader:
    _config = get_config_dict()

    def __init__(self):
        pass

    def get(self, section):
        return self._config[section]


if __name__ == '__main__':
    config = ConfigReader()
