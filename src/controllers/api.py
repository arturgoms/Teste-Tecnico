""" Api Controller

    Arquivo onde se encontra toda a lógica que rodará na rota '/api'

Todo:

    None

"""

import cgi
import json
import src.models.mysql as mysql

def getFields(environ):
        """
        getFields function:
            retorna os campos que chegam pelos metodos POST DELETE PUT
        """
        data_env = environ.copy()
        data_env['QUERY_STRING'] = ''
        data = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=data_env,
            keep_blank_values=True
        )
        return data

def api(environ, start_response):
    """
        api function:
            Lógica para a rota api
    """
    
    # Metodo POST, adiciona um contato no banco
    if environ['REQUEST_METHOD'] == 'POST':
        post = getFields(environ)
        db = mysql.MySQL()
        db.insert('users', {"nome":post['nome'].value, "sobrenome":post['sobrenome'].value, "endereco":post['endereco'].value })

    # Metodo DELETE, deleta um contato do banco
    if environ['REQUEST_METHOD'] == 'DELETE':
        delete = getFields(environ)
        db = mysql.MySQL()
        db.delete_where('users', 'id = {}'.format(delete['id'].value))

    # Metodo PUT, atualiza um contato 
    if environ['REQUEST_METHOD'] == 'PUT':
        put = getFields(environ)
        db = mysql.MySQL()
        db.update_where('users',"nome = '"+ put['nome'].value +"', sobrenome = '"+ put['sobrenome'].value +"', endereco = '"+ put['endereco'].value + "'", 'id = ' + put['id'].value)

    # Método GET, retorna todos os contatos no banco
    db = mysql.MySQL()
    json_data = db.select('users')
    html = str.encode(json.dumps(json_data))
    start_response('200 OK', [('Content-Type', 'text/json')])
    return [html]
