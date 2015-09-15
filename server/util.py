# !coding:utf-8



#raise httpError的方法
#raise tornado.web.HTTPError(500)

import redis
import tornado.web



# myCounter
def myCounter(page):
    # 设置访问计数
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    try:
        pageClickNum = r.get(page)
        if pageClickNum :
            pageClickNum = int(pageClickNum) + 1
        else:
            pageClickNum = 1

    except Exception, e:
        print "wrong"

    r.set(page,int(pageClickNum))
