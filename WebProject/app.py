from flask import Flask, render_template, request, flash, redirect
import re
from peewee import *

db = SqliteDatabase(
    "data.db"
)


class Ticket(Model):
    name = CharField()
    phone = CharField()
    is_active = BooleanField(default=True)

    class Meta:
        database = db


db.create_tables([Ticket])

app = Flask(__name__, template_folder="templates")
app.secret_key = "vwL,kFU{ETpSL`MhWBC@J.03z{2VUs7^?S"


@app.route("/call", methods=["POST"])
def on_call_post():
    name = request.form.get("name")
    phone = request.form.get("phone")

    phone_validate = re.compile("^\+[0-9]{11}$")
    if not(phone_validate.match(phone)):
        flash("Телефон указан неверно! Повторите попытку", "error")
        return redirect("/")
    ticket = Ticket.get_or_create(name=name, phone=phone)
    flash("Мы вам перезвоним!", "info")
    return redirect("/")

@app.route("/admin")
def get_tickets():
    return render_template("html/admin.html", Ticket=Ticket)

@app.route("/")
def get_index():
    return render_template("index.html")


@app.route("/classic")
def get_classic():
    return render_template("html/classic.htm")


@app.route("/eco")
def get_eco():
    return render_template("html/eco.htm")


@app.route("/ed")
def get_ed():
    return render_template("html/ed.htm")


@app.route("/erp")
def get_erp():
    return render_template("html/erp.htm")


@app.route("/inf")
def get_inf():
    return render_template("html/inf.htm")


@app.route("/ivt")
def get_ivt():
    return render_template("html/ivt.htm")


@app.route("/math")
def get_math():
    return render_template("html/math.htm")


@app.route("/phy")
def get_phy():
    return render_template("html/phy.htm")
