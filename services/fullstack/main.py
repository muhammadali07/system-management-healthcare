from flask import Flask

app = Flask(__name__)

@app.route("/")
<<<<<<< HEAD
def index():
    return "<p>Selamat datang di Klinik Terpadu</p>"

def login()

def regriter()
=======
def hello_world():
    return "<p>Hello, World!</p>"
>>>>>>> 671428f482041314d57a33303f390dfcdd4c50b1
