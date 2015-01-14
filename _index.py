def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html'),('Server','wqz_server')])
    return ["Hello,World!"]