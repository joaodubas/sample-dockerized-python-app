#!flask/bin/python

if __name__ == '__main__':
    import os
    from .app import app

    port = int(os.getenv('APP_PORT', '5000'))
    app.run(debug=True, port=port)
