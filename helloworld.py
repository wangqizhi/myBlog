#/usr/bin/python
#encoding=utf-8


import sys
import web

VERSION = "0.0.1a"


print  globals()
sys.exit()

urls = (
    '/','index'
	)

render = web.template.render('templates/')

def showVersion():
    ''' show Version '''
    print VERSION
    return VERSION


def testApp():
    pass
    

class index():
    "I am index"
    def GET(self):
        "learn get"
        return render.hello()



def main():
    showVersion()


if __name__ == '__main__':
    app = web.application(urls, globals())
    # main()
    app.run()