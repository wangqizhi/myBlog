#/usr/bin/python
#encoding=utf-8


import sys
import web

VERSION = "0.0.1a"


urls = (
    '/(.*)','hello'
	)
app = web.application(urls, globals())


def showVersion():
    ''' show Version '''
    print VERSION
    return VERSION

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'




def main():
    showVersion()


if __name__ == '__main__':
    # main()
    app.run()