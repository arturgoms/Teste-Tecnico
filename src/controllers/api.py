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
            retorna os campos que chegam pelos métodos POST DELETE PUT
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
    
    # Método POST, adiciona um contato no banco
    if environ['REQUEST_METHOD'] == 'POST':
        try:
            post = getFields(environ)
            db = mysql.MySQL()
            db.insert({"nome":post['nome'].value, "sobrenome":post['sobrenome'].value, "endereco":post['endereco'].value })
            start_response('200 OK', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"true"}))]
        except Exception as e:
            start_response('500 ERROR', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"false","error": 500,"method": "POST", "msg": "Não foi possível adicionar contato"}))]

    # Método DELETE, deleta um contato do banco
    if environ['REQUEST_METHOD'] == 'DELETE':
        try:
            delete = getFields(environ)
            db = mysql.MySQL()
            db.delete_where((delete['id'].value))
            start_response('200 OK', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"true"}))]
        except Exception as e:
            start_response('500 ERROR', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"false","error": 500,"method": "DELETE", "msg": "Não foi possível deletar contato"}))] 
        
    # Método PUT, atualiza um contato 
    if environ['REQUEST_METHOD'] == 'PUT':
        try:
            put = getFields(environ)
            db = mysql.MySQL()
            db.update_where([put['nome'].value,put['sobrenome'].value,put['endereco'].value], put['id'].value)
            start_response('200 OK', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"true"}))]
        except Exception as e:
            start_response('500 ERROR', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"false","error": 500,"method": "PUT", "msg": "Não foi possível atualizar contato"}))]

    # Método GET, retorna todos os contatos no banco
    if environ['REQUEST_METHOD'] == 'GET':
        try:
            db = mysql.MySQL()
            json_data = db.select()
            html = str.encode(json.dumps(json_data))
            start_response('200 OK', [('Content-Type', 'text/json')])
            return [html]
        except Exception as e:
            start_response('500 ERROR', [('Content-Type', 'text/json')])
            return [str.encode(json.dumps({"success":"false","error": 500,"method": "GET", "msg": "Não foi possível retornar tabela"}))]


