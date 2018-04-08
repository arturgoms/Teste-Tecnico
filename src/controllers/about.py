""" About Controller

    Arquivo onde se encontra toda a lógica que rodará na rota '/about'

Todo:

    None

"""

def about(environ, start_response):
    """
        about function:
            Lógica para a rota about
    """
    template = open('src/templates/about.html')
    html = str.encode(template.read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]
