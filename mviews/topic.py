#/usr/bin/python
# -*- coding: utf-8 -*-

import web



class topic:
    def __init__(self):
        pass

    def GET(self,name):
        if name == "1" :
            return web.template.render(base='base').one()
        else:
            return web.template.render().topic()
