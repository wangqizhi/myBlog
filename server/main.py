import tornado.ioloop
import tornado.web



import redis



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        try:
            indexClickNum = r.get('index')
        except Exception, e:
            indexClickNum = 0
        print indexClickNum
        r.set('index',indexClickNum + 1)
        print r.get('index')
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(10001)
    tornado.ioloop.IOLoop.current().start()
