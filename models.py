from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Choice(db.Model):
    __tablename__ = 'choises'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    choices = db.relationship('Pizza',backref='choice')

    def __repr__(self):
        return '<Choice: {title} Price: {price}>'.format(title=self.title, price=self.price)


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    choise_id = db.Column(db.Integer,db.ForeignKey('choises.id'))

    def __repr__(self):
        return '<Pizza: {title} Description: {desc}'.format(title=self.title, desc=self.description)
