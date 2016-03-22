import os, sys
import pycurl
import time
import IPy
import sys
import certifi
import requests, json


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/url/messages",
        auth=("api", "key-"),
        data={"from": "Master jx alert <postmaster@alert.catinmay.com>",
              "to": "jinxiao <admin@catinmay.com>",
              "subject": "Server Alert",
              "text": str(URL)+" EROR INFO: "+str(e)})


URL = ["https://catinmay.com:444","https://catinmay.com:555"]
for url in URL:
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.URL, URL)
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    c.setopt(pycurl.TIMEOUT, 5)
    c.setopt(pycurl.NOPROGRESS, 1)
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
    indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")
    c.setopt(pycurl.WRITEHEADER, indexfile)
    c.setopt(pycurl.WRITEDATA, indexfile)
    try:
        c.perform()
        NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
        # print(NAMELOOKUP_TIME)
        CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
        PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
        STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
        TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
        HTTP_CODE = c.getinfo(c.HTTP_CODE)
        SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
        HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
        SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)
        # PRINT RESULT
        print("HTTP状态码：%s" % (HTTP_CODE))
        print("DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME * 1000))
        print("建立连接时间：%.2f ms" % (CONNECT_TIME * 1000))
        print("准备传输时间：%.2f ms" % (PRETRANSFER_TIME * 1000))
        print("传输开始时间：%.2f ms" % (STARTTRANSFER_TIME * 1000))
        print("传输结束总时间：%.2f ms" % (TOTAL_TIME * 1000))
        print("下载数据包大小 %d bytes" % (SIZE_DOWNLOAD))
        print("HTTP头部大小： %d bytes" % (HEADER_SIZE))
        print("平均下载速度： %d bytes/s" % (SPEED_DOWNLOAD))

        indexfile.close()
        c.close()
        sys.exit()
    except Exception as e:
        print("sending email ...")
        send_simple_message()
        print("email sends ok")
        sys.exit()