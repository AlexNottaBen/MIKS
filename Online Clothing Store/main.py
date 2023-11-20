#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect

from app import app
from Product import Product
from ProductPhoto import ProductPhoto
from Purchase import Purchase


@app.route("/")
def index():
    products = Product.query.all()
    photos = ProductPhoto.query.all()
    return render_template("index.html", products=products, photos=photos)


@app.route("/product/<int:id>")
def product_page(id: int):
    try:
        product = Product.query.filter_by(id=id).first()
        photos = ProductPhoto.query.all()
        other_products_type = Product.query.filter_by(
            type_of_product=product.type_of_product
        )
        other_products_collection = Product.query.filter_by(
            collection=product.collection
        )
        return render_template(
            "product.html",
            product=product,
            photos=photos,
            other_products_type=other_products_type,
            other_products_collection=other_products_collection,
        )
    except (AttributeError, UnboundLocalError) as exception:
        print(exception)
        return redirect("/")


@app.route("/buy")
def buy():
    quantity = request.args["quantity"]
    price = request.args["price"]
    purchase = Purchase(price, quantity)
    url = purchase.get_url()
    return redirect(url)


def main():
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
