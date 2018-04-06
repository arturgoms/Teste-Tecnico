""" Index Controller

    Arquivo onde se encontra toda a lógica que rodará na rota 404

Todo:

    None

"""

def error_404(start_response):
    """
        error_404 function:
            Lógica para a rota 404 (not found)
    """
    template = open('src/templates/404.html')
    html = str.encode(template.read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]
