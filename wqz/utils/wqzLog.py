#encoding:utf-8

import time


class wqzLog(object):
    """log工具"""

    def __init__(self ,logLevel ,fileName=None):
        # super(wqzLog, self).__init__()
        self.logLevel = logLevel
        self.fileName = fileName

    #实时标准输出
    def stOut(self,logFormat):
        # if self.level == "Debug":
        print logFormat

    #文件记录
    def fileOut(self,logFormat):
        try:
            fn = open(self.fileName,"a")
            fn.write(logFormat)
            fn.close()
        except Exception, e:
            raise e


    def log(self ,logTag ,logContent):
        #格式化日志
        logFormat = " ".join(["["+time.ctime()+"]" ,"[*"+logTag+"]" ,logContent ,"\n"])

        #level:debug ,打印及记录所有日志
        if self.logLevel == "Debug":
            self.stOut(logFormat)
            self.fileOut(logFormat)
        #level:Dev ,打印所有日志
        elif self.logLevel == "Dev":
            self.stOut(logFormat)
        #level:Test ,打印及记录所有错误、警告日志
        elif self.logLevel == "Test":
            if logTag == "Error" or logTag == "Warning":
                self.stOut(logFormat)
                self.fileOut(logFormat)
        #level:Product ,记录所有错误日志
        elif self.logLevel == "Product":
            if logTag == "Error":
                self.fileOut(logFormat)
        #level:Files ,记录所有日志
        elif self.logLevel == "Files":
            self.fileOut(logFormat)
        #其他level 无日志
        else:
            pass






if __name__ == '__main__':
    # log = wqzLog("debug")
    wqzLog("Files" ,fileName="test.log").log("Ersafdsror","Hello,world")
