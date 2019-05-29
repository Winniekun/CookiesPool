"""
@Time : 2019/5/28 下午5:42
@Author : kongwiki
@File : config.py
@Email : kongwiki@163.com 
"""
# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码
REDIS_PASSWORD = None

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，相关的配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，相关配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = 'localhost'
API_PORT = 5003

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
