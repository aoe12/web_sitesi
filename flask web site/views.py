from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def anasayfa():
    return render_template("anasayfa.html", user=current_user)

@views.route("/hastaliklar")
def hastaliklar():
    return render_template("hastaliklar.html", user=current_user)

@views.route("/sulama+bilgileri")
def sulamabilgileri():
    return render_template("sulamasecimleri.html", user=current_user)
