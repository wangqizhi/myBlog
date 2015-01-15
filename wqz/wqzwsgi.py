#encoding:utf-8



class WqzWsgi(object):
    """逻辑主体"""


    acceptStatic = True

    arbitration = (True,"pass")

    repStout = "Welcom，Use Wqz web framework"

    repStatus = "200"

    repHeaders = [('Content-Type','text/html'),('Server','wqz_wsgi')]


    def __init__(self, env):
        # super(ClassName, self).__init__()
        self.env = env
        try:
            """
            路由判断
            """
            import wqzUrls
            self.checkRouter(wqzUrls.wqzRouter,self.env["PATH_INFO"])
            # print "check over",self.arbitration[0]
            if self.arbitration[0] == False:
                self.repStout = "404 not found"
                self.repStatus = "404"
            else:
                self.showRouter(wqzUrls.wqzRouter)

        except Exception, e:    
            arbitration = (False,str(e))
            # 查错打印
            # print "*****wrong******"
            # print e

    def checkRouter(self,routerList,uriChecked):
        """
        检查是否在路由中
        """
        for v,k in routerList:
            if k == uriChecked:
                return 
        self.arbitration = (False,"404")

    def showRouter(self,routerList):
        for v,k in routerList:
            if self.env["PATH_INFO"] == "/img":
                # print "*******show Debug:",open("favicon.ico","rb").read()
                self.repStout = open("favicon.ico").read()
                self.repHeaders = [('Content-Type','image/x-icon'),('Server','wqz_wsgi')]
            elif self.env["PATH_INFO"] == "/showenv":
                self.repStout = str(self.env)
            elif self.env["PATH_INFO"] == "/test.html":
                self.repStout = open("templates/showenv.html").read()
                self.repHeaders = [('Content-Type','text/html'),('Server','wqz_wsgi')]
            else:
                print "***** in else"
                self.repStout = "in route"







if __name__ == '__main__':
    import sys
    sys.path.append("..")
    wqz = WqzWsgi({"PATH_INFO":"/index"})