from flask import render_template, session, redirect, request
from shop_application import app
from shop_application.models import Category
from shop_application.forms import UserOrderData


@app.route("/")
def main():
    categories = Category.query.all()
    return render_template("main.html", categories=categories)

@app.route("/addtocart/<meal_id>/")
def add_to_card(meal_id: int):
    cart = session.get("cart", {})
    meal_cart_count = cart.get(meal_id, 0)
    cart.update({meal_id: 1 if not meal_cart_count else meal_cart_count + 1})
    session["cart"] = cart
    print(session["cart"])
    return redirect("/cart/")


@app.route("/cart/", methods=["GET", "POST"])
def cart():
    form = UserOrderData()
    if session.get("user", None) is None:
        form.address.errors = []
        form.address.errors.append("Чтобы сделать заказ – войдите/зарегистрируйтесь")
        return render_template("cart.html", form=form, session=session)
    if request.method == "POST":
        if not form.validate_on_submit():
            return render_template("cart.html", form=form, session=session)
        print(form.name.data)
        print(form.address.data)
        print(form.email.data)
        print(form.phone_number.data)

    return render_template("cart.html", form=form, session=session)


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
