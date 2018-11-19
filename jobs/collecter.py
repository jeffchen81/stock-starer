# -*- coding: utf-8 -*-
# another: Jeff.Chen
# 采集数据，写入文件
import requests
import datetime
import sys


# 解决中文Unicode问题
reload(sys)
sys.setdefaultencoding('utf8')


def collect_stock(stock_code):
    """
    采集，反馈文本
        :param stock_code: 
    """
    url = "http://hq.sinajs.cn/list={}".format(stock_code)

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "8cb8b839-fbbf-48fd-b8a8-103a328c9f16"
        }

    response = requests.request("GET", url, headers=headers)

    #print(response.text)
    return str(response.text)


def now_date():
    """
    当前yyyy-mm-dd
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")


if __name__ == "__main__":
    data_text = collect_stock('sh603259')
    data_filename = now_date() + ".txt"

    with open(data_filename, 'a') as f:
        f.write(data_text)
