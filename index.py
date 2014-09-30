#/usr/bin/python
# -*- coding: utf-8 -*-

import web


# 导入views
from mviews.index import *
from mviews.info import *


# 路由
urls = (
    '/', 'index',
    '/getinfo', 'info',
)


# 自带webserver
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()