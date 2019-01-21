# -*- coding: utf-8 -*-
# another: Jeff.Chen
# 股票执行动作
import os


def read_txt(data_file):
    """
    读取股票数据文件，反馈字典
        :param data_file: 股票数据文件名
    """
    with open(data_file, 'r') as f:
        for line in f.readlines():
            # print(line.strip())
            # TODO 测试1条
            change_model(line.strip())
            break
    pass


def change_model(data_line):
    """
    数据文本行转为模型
        :param data_line: 数据行
    """
    # print(data_line)
    data_array = str(data_line).split('"')
    # print(data_array[1])
    core_row = data_array[1].split(",")
    for d in core_row:
        print (d)
    # print(data for data in core_row)
    pass


if __name__ == '__main__':
    print(os.getcwd())

    # 读取指定文件
    # with open(os.getcwd() + '/2018-11-26.txt', 'r') as f:
    #     for line in f.readlines():
    #         print(line.strip())
    #         # TODO 测试1条
    #         break
    read_txt(os.getcwd() + '/2018-11-26.txt')

    pass
