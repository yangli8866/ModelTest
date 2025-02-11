import subprocess

import pytest

from utils.parser import Paser
from utils.utils import Util

import os

# def __main__():
    # 登录，获取鉴权token
    # Util.auto_login()

    # pytest.main('')
    # # mark为选择要运行的case的mark
    # mark = 'tech'
    #
    # # 要执行的case的json文件列表
    # api_list = []
    #
    # # 要执行的case的json文件所在路径，会执行这个路径下所有的json文件
    # api_file_path = ''
    # if api_file_path:
    #     api_list = Util.get_api_list(api_file_path)
    # # 调用parser解析方法
    # if api_list:
    #     # 解析生成pytets
    #     Paser.paser_test_file(api_list)
    #     # 运行pytest
    #     pytest.main('')
    # else:
    #     print('no case to run')


if __name__=='__main__':
    Util.auto_login()




