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
        
        user1 = UserBuilder(username, email, password, birthday) \
            .set_full_name(full_name) \
            .set_home_address(home_address) \
            .set_phone_number(phone_number) \
            .set_gender(gender) \
            .set_card_number(card_number) \
            .set_cardholder_name(cardholder_name) \
            .set_card_expire_month(card_expire_month) \
            .set_card_expire_year(card_expire_year) \
            .build()
        
        return f'<h1>{user1}</h1>'.replace("\n","<br>")


def main():
    app.run(debug=True, port=5001)


if __name__ == "__main__":
    main()
