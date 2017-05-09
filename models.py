from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    choices = db.relationship('Choice', back_populates='pizza')

    def __repr__(self):
        return '<Pizza: {title} Description: {desc}'.format(title=self.title, desc=self.description)


class Choice(db.Model):
    __tablename__ = 'choice'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    pizza = db.relationship('Pizza', back_populates='choices')

    def __repr__(self):
        return '<Choice: {title} Price: {price}>'.format(title=self.title, price=self.price)



