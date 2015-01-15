#encoding:utf-8



class WqzWsgi(object):
    """逻辑主体"""

    arbitration = (True,"pass")

    repStout = "Hello,World"

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
            print "*****wrong******"
            print e

    def checkRouter(self,routerList,uriChecked):
        """
        检查是否在路由中
        """
        for v,k in routerList:
            if k == uriChecked:
                return 
        self.arbitration = (False,"404")

    def showRouter(self,routerList):
        self.repStout = "in route"





if __name__ == '__main__':
    import sys
    sys.path.append("..")
    wqz = WqzWsgi({"PATH_INFO":"/index"})