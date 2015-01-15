#encoding:utf-8
from wqz.wqzwsgi import WqzWsgi

# out =WqzWsgi("1")
# print out.repStatus

def application(env, start_response):
    out =WqzWsgi(env)
    start_response(out.repStatus,out.repHeaders)
    return [out.repStout]