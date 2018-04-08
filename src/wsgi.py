#!/usr/bin/env python

""" WSGI File

    Arquivo onde se concentra as principais funções do servidor, utilizado pelo "manager.py"

Todo:

    None

"""

import src.settings as conf
from src.controllers.index import (index)
from src.controllers.error_404 import (error_404)
from src.controllers.api import (api)
from src.controllers.layout import (layout)
from src.controllers.about import (about)

def static(start_response, path, type):
    """
        static function:
            Função que recebe o local e o tipo de arquivo estático
            e retorna seu conteúdo para a rota.
    """
    static_file = open(conf.STATIC_URL + path)
    html = str.encode(static_file.read())
    start_response('200 OK', [('Content-Type', 'text/'+ type)])
    return [html]

def router(environ, start_response):
    """
        router function:
            Função que determina qual controller será chamado na rota
            requisitada.
    """
    if environ['PATH_INFO'] == '/':
        return layout(environ, start_response)

    elif environ['PATH_INFO'] == '/index':
        return index(environ, start_response)

    elif environ['PATH_INFO'] == '/api':
        return api(environ, start_response)

    elif environ['PATH_INFO'] == '/about':
        return about(environ, start_response)

    elif environ['PATH_INFO'] == '/css/style.css':
        return static(start_response, '/css/style.css', 'css')

    elif environ['PATH_INFO'] == '/js/main.js':
        return static(start_response, '/js/main.js', 'js')

    return error_404(start_response)
