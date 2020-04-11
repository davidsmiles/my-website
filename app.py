import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from models.contact import Contact


app = Flask(__name__)

load_dotenv(".env")
app.config.from_object('default_config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        user = Contact(name=name, email=email, message=message)
        user.save_to_db()

        return f'Thank you {name} {email} for your message'


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0')
