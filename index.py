#/usr/bin/python
#encoding = utf-8

import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello1, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()