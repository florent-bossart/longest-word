from wsgi import app


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process will serve the app
    app.run(host='127.0.0.1', port=8080, debug=True)
