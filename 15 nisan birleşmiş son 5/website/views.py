from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def anasayfa():
    return render_template("index.html", user=current_user)

@views.route('/anasayfa2')
@login_required
def anasayfa2():
    return render_template("index2.html", user=current_user)

@views.route('/hakkinda')
def hakkinda():
    return render_template("hakkinda.html", user=current_user)

@views.route('/hakkinda2')
def hakkinda2():
    return render_template("hakkinda2.html", user=current_user)

@views.route("/hastaliklar")
def hastaliklar():
    return render_template("hastaliklar.html", user=current_user)

@views.route("/hastaliklar2")
def hastaliklar2():
    return render_template("hastaliklar2.html", user=current_user)

@views.route("/sulama+bilgileri")
def sulamabilgileri():
    return render_template("sulamasecimleri.html", user=current_user)
