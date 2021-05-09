from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__, template_folder="templates", static_folder="static")

@views.route('/')
def anasayfa():
    return render_template("index.html")

@views.route('/anasayfa2')
@login_required
def anasayfa2():
    return render_template("index2.html", user=current_user)

@views.route('/hakkinda')
def hakkinda():
    return render_template("hakkinda.html")

@views.route('/hakkinda2')
@login_required
def hakkinda2():
    return render_template("hakkinda2.html", user=current_user)

@views.route("/hastaliklar")
def hastaliklar():
    return render_template("hastaliklar.html")

@views.route("/hastaliklar2")
@login_required
def hastaliklar2():
    return render_template("hastaliklar2.html", user=current_user)

@views.route("/sulama+bilgileri", methods=['GET', 'POST'])
@login_required
def sulamabilgileri():
    if request.method == 'POST':
        gun = request.form.get('gun')
        print("**********")
        print("Gün: ")
        print(gun)
    
    if request.method == 'POST':
        ay = request.form.get('ay')
        print("**********")
        print("Ay: ")
        print(ay)

    if request.method == 'POST':
        yıl = request.form.get('yıl')
        print("**********")
        print("Yıl: ")
        print(yıl)

    if request.method == 'POST':
        urun = request.form.get('urun')
        print("**********")
        print("Ürün: ")
        print(urun)

    if request.method == 'POST':
        alan = request.form.get('alan')
        print("**********")
        print("Alan Buyuklugu: ")
        print(alan)
        print("**********")
        return redirect(url_for('views.sulamabilgileri'))

    return render_template("sulamasistemi.html", user=current_user)
