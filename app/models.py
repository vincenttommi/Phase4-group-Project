from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
# from sqlalchemy_serializer impor, SerializerChain




db = SQLAlchemy()

class Car(db.Model):
    __tablename__ = 'cars'
    
    id = db.Column(db.Integer, primary_key=True)
    car_make = db.Column(db.String(50), nullable=False)
    car_model = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealers.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('buyers.id'), nullable=True)
    dealer = db.relationship('Dealer', backref=db.backref('cars'))
    owner = db.relationship('Buyer', backref=db.backref('car', uselist=False))
    orders = db.relationship('Order', backref='car')

    serialize_rules = ('-dealer.cars', '-owner.orders',)

class Dealer(db.Model):
    __tablename__ = 'dealers'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    # serialize_rules = (
    #     SerializerChain()
    #     .include('cars')
    # )

class Buyer(db.Model):
    __tablename__ = 'buyers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    # serialize_rules = (
    #     SerializerChain()
    #     .include('cars')
    # )

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    car_price = db.Column(db.Float, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyers.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
