#encoding:utf-8
from wqz.wqzwsgi import WqzWsgi

# out =WqzWsgi("1")
# print out.repStatus

def application(env, start_response):
    wqz =WqzWsgi(env)
    start_response(wqz.repStatus,wqz.repHeaders)
    return [wqz.repStout]