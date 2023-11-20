#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy


app = Flask(
    import_name=__name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product/<int:id>")
def product_page(id: int):
    return render_template("product.html")


def main():
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
