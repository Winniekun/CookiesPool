"""
@Time : 2019/5/28 下午5:43
@Author : kongwiki
@File : importer.py
@Email : kongwiki@163.com 
"""
import requests
from pool.db import RedisClient

conn = RedisClient('acounts', 'weibo')


def set(accout, sep='----'):
    username, password = accout.split(sep)
    result = conn.set(username, password)
    print("账号", username, "密码", password)
    print("录入成功" if result else "录入失败")


def scan():
    print("请输入对应格式的账号密码")
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    scan()