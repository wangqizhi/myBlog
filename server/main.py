#! coding:utf-8

import tornado.ioloop
import tornado.web

from tornado.options import define,options,parse_command_line

from util import myCounter




class MainHandler(tornado.web.RequestHandler):
    def get(self):

        myCounter('index')
        import time,os
        # self.write("Hello, world")
        varDict = {
        'publishData':time.ctime(),
        'dirData':os.listdir('./blogs'),
        'fileData':os.stat('./blogs/hello3.blog')
        }
        self.render('index.html',varDict=varDict)



if __name__ == "__main__":
    # 启动端口
    define("port",default=10001,help="port of running")
    try:
        parse_command_line()
    except Exception, e:
        pass

    application = tornado.web.Application([
        (r"/", MainHandler),
    ],
        template_path = './tpl/',
    )
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
