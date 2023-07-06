from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Car(db.Model, SerializerMixin):
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

    def serialize(self):
        return {
            'id': self.id,
            'car_make': self.car_make,
            'car_model': self.car_model,
            'price': self.price,
            'year': self.year,
            'image': self.image,
            'dealer_id': self.dealer_id
        }

class Dealer(db.Model, SerializerMixin):
    __tablename__ = 'dealers'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'email': self.email,
            'phone_number': self.phone_number
        }

class Buyer(db.Model, SerializerMixin):
    __tablename__ = 'buyers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
        }

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    car_price = db.Column(db.Float, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyers.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'car_price': self.car_price,
            'buyer_id': self.buyer_id,
            'order_date': self.order_date.strftime('%Y-%m-%d %H:%M:%S') 
        }
