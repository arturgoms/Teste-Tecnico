import cgi
from src.controllers.index import *
from src.controllers.error_404 import *

def app(environ, start_response):

    if environ['PATH_INFO'] == '/':
        html = index(environ)
    else:
        html = error_404(environ)
     
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]