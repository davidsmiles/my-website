from datetime import datetime

from db import db

from libs.sendmail import Sendmail


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    time_sent = db.Column(db.String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_sent = datetime.now().strftime('%d-%m-%Y %H:%M')

    def send_me_mail(self):
        subject = f'From {self.name} {self.email}'
        text = self.message

        return Sendmail.send_email(self.email, subject, text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
