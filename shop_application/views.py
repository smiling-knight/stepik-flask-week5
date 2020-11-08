from flask import render_template
from shop_application import app

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/cart/")
def cart():
    return render_template("cart.html")


@app.route("/account/")
def account():
    return render_template("account.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/register/")
def register():
    return render_template("registered.html")


@app.route("/logout/")
def logout():
    pass


@app.route("/ordered/")
def ordered():
    return render_template("ordered.html")
