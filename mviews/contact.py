#/usr/bin/python
# -*- coding: utf-8 -*-

import web



class contact:
    def __init__(self):
        pass

    def GET(self):
        name = "contact test"
        return web.template.render('templates/').index(name)

