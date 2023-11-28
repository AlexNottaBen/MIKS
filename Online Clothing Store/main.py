#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect

from app import app
from Product import Product
from Purchase import Purchase
from ProductPage import ProductPage
from ProductPhoto import ProductPhoto
from AdditionalProducts import AdditionalProducts


@app.route("/")
def index():
    products = Product.query.all()
    photos = ProductPhoto.query.all()
    return render_template("index.html", products=products, photos=photos)


@app.route("/product/<int:id>")
def product_page(id: int):
    product = Product.query.filter_by(id=id).first_or_404()
    photos = ProductPhoto.query.all()

    additional_products: AdditionalProducts = AdditionalProducts()
    product_page: ProductPage = ProductPage(additional_products)

    # Call the function to display additional products
    return product_page.show_additional_products(product, photos)


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
