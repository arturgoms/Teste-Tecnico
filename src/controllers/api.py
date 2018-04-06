""" Api Controller

    Arquivo onde se encontra toda a lógica que rodará na rota '/api'

Todo:

    None

"""

import cgi
import json
import src.models.mysql as mysql

def api(environ, start_response):
    """
        api function:
            Lógica para a rota api
    """
    
    if environ['REQUEST_METHOD'] == 'POST':
        html = str.encode(json.dumps({"REQUEST_METHOD": "POST"}))
    else:
        db = mysql.MySQL()
        json_data = db.select('users')
        html = str.encode(json.dumps(json_data))

    start_response('200 OK', [('Content-Type', 'text/json')])
    return [html]
