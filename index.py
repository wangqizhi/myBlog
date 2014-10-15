#/usr/bin/python
# -*- coding: utf-8 -*-

import web


# 导入views
from mviews.index import *
from mviews.info import *
from mviews.contact import *
from mviews.topic import *


# 路由
urls = (
    '/', 'index',
    '/getinfo', 'info',
    '/contact', 'contact',
    '/topic/(.*)', 'topic',
)


# 自带webserver
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()