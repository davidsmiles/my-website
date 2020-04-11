from flask import Flask, render_template, request
from contact import Contact


app = Flask(__name__)
app.secret_key = 'iamdoingwell'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://david:a@localhost:5432/david'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_all():
    db.create_all()


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
