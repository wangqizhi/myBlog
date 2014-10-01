#/usr/bin/python
# -*- coding: utf-8 -*-

import web

class index:
    def __init__(self):
        pass

    def GET(self):
    	return web.template.render('templates/').index()
        # return "Hello1, world!"

