#! /usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from UserBuilder import UserBuilder


app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full-name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        birthday = request.form['birthday']
        home_address = request.form['home-address']
        phone_number = request.form['phone-number']
        gender = request.form['gender']
        card_number = request.form['card-number']
        card_expire_month = request.form['month']
        card_expire_year = request.form['year']
        cardholder_name = request.form['cardholder-name']
        
        if password != confirm_password:
            return "<h1>Passwords do not match!<h1>"
        
        user_builder = UserBuilder(username, email, password, birthday)
        
        user_builder.full_name = full_name
        user_builder.home_address = home_address
        user_builder.phone_number = phone_number
        user_builder.gender = gender
        user_builder.card_number = card_number
        user_builder.cardholder_name = cardholder_name
        user_builder.card_expire_month = card_expire_month
        user_builder.card_expire_year = card_expire_year
        
        user = user_builder.build()
        
        return f'<h1>{user}</h1>'.replace("\n","<br>")


def main():
    app.run(debug=True, port=5001)


if __name__ == "__main__":
    main()
