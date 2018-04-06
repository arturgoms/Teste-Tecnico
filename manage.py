#!/usr/bin/env python

from src.wsgi import app
import src.settings as conf
class server():
    def __init__(self):
        try:
            from wsgiref.simple_server import make_server
            httpd = make_server('', conf.PORT, app)
            print('Serving on port {}'.format(conf.PORT))
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Shutdown Server via Keyboard.')

if __name__ == '__main__':
    server()