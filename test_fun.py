class Wangqizhi(object):
    """test for Wangqizhi"""
    # name = "myNameWqz"
    def __init__(self):
        super(Wangqizhi, self).__init__()
        print "I am init"
        
    def __getattr__(self,name):
        print "in get attr "+ name

    def __setattr__(self,name,value):
        print "show:"+name
        print value+" <==end"





def main():
    wqz = Wangqizhi
    # wqz.test = "wqz1"

    # print wqz.test
    wqz()



if __name__ == '__main__':
    main()