#!/usr/bin/env python

""" Teste Técnico

Criar uma página única (Single page application) de cadastro
de pessoas (nome, sobrenome e endereço) utilizando HTML,
Javascript, CSS, MySQL e PHP (ou Python).

Todo:

    None

"""
from src.wsgi import router
import src.settings as conf

class Server():
    """
        Server class:
            Habilita o servidor na porta definida nas configurações e com a função "router"
            para definir as rotas.
    """
    def __init__(self):
        try:
            from wsgiref.simple_server import make_server
            httpd = make_server('', conf.PORT, router)
            print('Serving on port {}'.format(conf.PORT))
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Shutdown Server via Keyboard.')

if __name__ == '__main__':
    Server()
