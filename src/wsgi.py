import cgi
import src.settings as conf
from src.controllers.index import *
from src.controllers.error_404 import *

def static(start_response, path, type):
    f = open( conf.STATIC_URL + path)
    html = str.encode(f.read())
    start_response('200 OK', [('Content-Type', 'text/'+ type)])
    return [html]

def router(environ, start_response):

    if environ['PATH_INFO'] == '/':
        return index(environ, start_response)

    elif environ['PATH_INFO'] == '/css/style.css':
        return static(start_response, '/css/style.css', 'css')

    elif environ['PATH_INFO'] == '/js/main.js':
        return static(start_response, '/js/main.js', 'js') 

    else:
        return error_404(environ, start_response)