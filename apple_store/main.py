#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from random import choice

from DeviceFactory import OriginalRefurbishedDeviceFactory, ReplicaDeviceFactory

app = Flask(__name__, template_folder="templates", static_folder="static")

items = []


@app.route('/', methods=["GET", "POST"])
def index():
    # Create a factory object based on a random selection
    if choice([True, False]):
        factory = OriginalRefurbishedDeviceFactory()
    else:
        factory = ReplicaDeviceFactory()

    # Creating a device using a factory
    device = factory.create_device()

    items.append(device)

    return render_template('index.html', items=items)


def main():
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
