""" Index Controller

    Arquivo onde se encontra toda a lógica que rodará na rota '/'

Todo:

    None

"""

def layout(environ, start_response):
    """
        index function:
            Lógica para a rota index
    """
    template = open('src/templates/layout.html')
    html = str.encode(template.read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]
