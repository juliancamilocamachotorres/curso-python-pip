import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
            <html>
            <head>
            <title>Test</title>
            </head>
            <body>
            <h1>Esta funcionado el web-server</h1>
            <p>Soy Julian</p>
            </body>
            </html>
            """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()