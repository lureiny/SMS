from flask import Flask, request
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from flask import Blueprint
import json
from common_units.small_tools import *


teacher = Flask(__name__)
json_rpc = JSONRPC(teacher, "teacher")


@json_rpc.method("login")
def login(username, password):
    """
    用户登陆判断接口;
    :param username: 用户名
    :param password: 密码
    :return:
    """
    pass


@json_rpc.method("manage")
def manage(info):
    """
    教师信息更改接口
    :param info: 教师信息
    :return:
    """
    pass
