#/usr/bin/python
# -*- coding: utf-8 -*-

import web



class info:
    def __init__(self):
        pass

    def GET(self):
        return web.ctx.env

