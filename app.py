from flask import Flask
imort OS

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Lilian"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
