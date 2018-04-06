def error_404(environ):
        f = open('src/templates/404.html')
        html = str.encode(f.read())
        return html
