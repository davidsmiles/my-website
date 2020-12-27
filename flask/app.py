# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
#
from dotenv import load_dotenv
from flask import Flask, render_template, request

from models.contact import Contact

# sentry_sdk.init(
#     dsn="https://198f1994bed4409d9b43632d53d3c197@o397526.ingest.sentry.io/5253062",
#     integrations=[FlaskIntegration()]
# )

app = Flask(__name__)

load_dotenv(".env")
app.config.from_object('default_config')
# app.config.from_envvar('APPLICATION_SETTINGS')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test_index():
    return "Hello david james"


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        user = Contact(name=name, email=email, message=message)
        user.save_to_db()
        # user.send_me_mail()

        return render_template('contact.html', name=name)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=8080)
