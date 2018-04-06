def error_404(environ, start_response):
        f = open('src/templates/404.html')
        html = str.encode(f.read())
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [html]
