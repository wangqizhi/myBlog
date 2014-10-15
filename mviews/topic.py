#/usr/bin/python
# -*- coding: utf-8 -*-

import web



class topic:
    def __init__(self):
        pass

    def GET(self,name):
        return web.template.render().topic(name)

