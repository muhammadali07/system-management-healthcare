from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/main_menu")
def main_menu():
    return render_template("menu_pasien.html")

@app.route("/admin_menu")
def admin_menu():
    return render_template("admin_menu.html")