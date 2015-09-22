#! /usr/bin/env python
#! coding:utf-8

# By wqz
#  
# Licensed None




'''Start up'''

from __future__ import division


# by pythonSelf
import logging
import time
import os

# thirdPart
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define,options,parse_command_line

# by mySelf
from util import myCounterAdd,myCounterGet




def listDirFiles(dir,filter):
    '''listDirFiles(目录,过滤器):遍历blog，找出过滤后缀的文件数组'''
    fileArray = {}

    for i in os.walk(dir):
        if i[2] != 0 :
            for j in i[2]:
                try:
                    if j.split(".")[1] == filter:
                        # fileArray.append(j.split(".")[0]
                        fileTime = os.stat(i[0]+"/"+j).st_ctime
                        fileArray[j.split(".")[0]] = fileTime
                except Exception, e:
                    print "Type Wrong"
                
    return fileArray

     


class MainHandler(tornado.web.RequestHandler):
    '''uri: http://host:port/'''
    def get(self):

        def getTimeFromTs(timestamp):
            '''getTimeFromTs'''
            xtime = time.localtime(timestamp)
            return time.strftime('%Y-%m-%d %H:%M',xtime)
        myCounterAdd('index')
        # self.write("Hello, world")
        logging.info('IP(%s) access /'%str(self.request.headers['Rip']))
        varDict = {
            'publishData':time.ctime(),
            # 'dirData':listDirFiles('./blogs','html'),
            'dirData':listDirFiles(options.blog,'html'),
            'hitCounts':myCounterGet('index'),
        }
        self.render('index.html',varDict=varDict,getTimeFromTs=getTimeFromTs)

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        import json
        x = {"r":"ok","num":10,"test001":"helloworld"}
        self.set_header('Content-Type','application/json')
        self.write(json.dumps(x)) 
       

class AdminHandler(tornado.web.RequestHandler):
     '''uri: http://host:port/admin'''
     def get(self):
        myCounterAdd('admin')
        self.write("hello,admin")
          



if __name__ == "__main__":
    
    NOWDIR = os.path.dirname(os.path.realpath(__file__))

    define("port",default = 10001 ,help = "port of running")# 启动端口
    define("logDir",default = NOWDIR + '/log/',help = "dir of log")# 日志目录
    define("level",default = 'info',help = "level of logging")# 日志级别
    options.logging = options.level
    # 日志配置,
    logging.basicConfig(
        # level=logging.DEBUG,
        filename = ''.join([options.logDir,time.strftime('%Y%m%d'),'.log']),
        filemode='a',
        # datefmt='',
    )
    #####tips:日志目录创建的功能还没有完成，已知bug：没有日志目录的情况下会500

    define("blog",default = NOWDIR + "/blogs",help = "dir of blogShow")

    try:
        parse_command_line()
    except Exception, e:
        print "error-parse_command_line():%s"%e



    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/admin", AdminHandler),
        (r"/test", TestHandler),
    ],
        template_path = NOWDIR + '/tpl/',
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
