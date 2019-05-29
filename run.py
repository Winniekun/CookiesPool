"""
@Time : 2019/5/29 上午11:09
@Author : kongwiki
@File : run.py
@Email : kongwiki@163.com 
"""
from pool.scheduler import Scheduler


def main():
    s = Scheduler()
    s.run()


if __name__ == '__main__':
    main()