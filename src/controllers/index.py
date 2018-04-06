def index(environ):
        f = open('src/templates/index.html')
        html = str.encode(f.read())

        if environ['REQUEST_METHOD'] == 'POST':
            post_env = environ.copy()
            post_env['QUERY_STRING'] = ''
            post = cgi.FieldStorage(
                fp=environ['wsgi.input'],
                environ=post_env,
                keep_blank_values=True
            )
            html = str.encode("Hello, %s!"%post['name'].value)

        return html
