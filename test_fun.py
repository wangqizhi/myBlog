class Wangqizhi(object):
    """test for Wangqizhi"""
    name = "myNameWqz"
    def __init__(self):
        # super(Wangqizhi, self).__init__()
        print "I am init"
        
    def __getattr__(self,name):
        print "in get attr "+ name
        def helloworld():
            print "hello,in helloworld"
        return helloworld

    def __setattr__(self,name,value):
        print "show:"+name
        print value+" <==end"





def main():
    wqz = Wangqizhi()

    # wqz.test = "wqz1"

    wqz.test()
    # wqz.name = "1"
    # print wqz.name



if __name__ == '__main__':
    main()