from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("01_index.html")

@app.route("/login")
def login():
    return render_template("02_login.html")

@app.route("/register")
def register():
    return render_template("03_register.html")

@app.route("/admin_menu")
def admin_menu():
    return render_template("04_admin_menu.html")

@app.route("/biodata_admin")
def biodata_admin():
    return render_template("05_biodata_admin.html")

@app.route("/edit_biodata")
def edit_biodata():
    return render_template("06_edit_biodata.html")

@app.route("/tambah_dokter")
def tambah_dokter():
    return render_template("07_tambah_dokter.html")

@app.route("/daftar_antrian")
def daftar_antrian():
    return render_template("08_daftar_antrian.html")








# u/ pasien dikerjakan hendris
@app.route("/main_menu")
def main_menu():
    return render_template("menu_pasien.html")

@app.route("/janji_temu")
def janji_temu():
    return render_template("janji_temu.html")