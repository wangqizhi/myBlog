import tornado.ioloop
import tornado.web



import redis



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        try:
            indexClickNum = r.get('index')
            if indexClickNum :
                indexClickNum = int(indexClickNum) + 1
            else:
                indexClickNum = 1

        except Exception, e:
            print "wrong"

        r.set('index',int(indexClickNum))
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(10001)
    tornado.ioloop.IOLoop.current().start()
