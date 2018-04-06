import cgi
import src.settings as conf
from src.controllers.index import *
from src.controllers.error_404 import *

def router(environ, start_response):

    if environ['PATH_INFO'] == '/':
        html = index(environ)
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [html]

    elif environ['PATH_INFO'] == '/css/style.css':
        f = open( conf.STATIC_URL + 'css/style.css')
        html = str.encode(f.read())
        start_response('200 OK', [('Content-Type', 'text/css')])
        return [html]

    elif environ['PATH_INFO'] == '/js/main.js':
        f = open( conf.STATIC_URL + 'js/main.js')
        html = str.encode(f.read())
        start_response('200 OK', [('Content-Type', 'text/js')])
        return [html]        

    else:
        html = error_404(environ)
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [html]