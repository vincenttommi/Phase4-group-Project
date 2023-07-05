from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource
from wtforms import Form, StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange, URL
from datetime import datetime

from models import db, Car, Dealer, Buyer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db.init_app(app)
   
# Perform database migrations
migrate = Migrate(app, db)

<<<<<<< HEAD
# Enable CORS
CORS(app)

# Initialize flask-restful API
api = Api(app)

class CarForm(Form):
    car_make = StringField('Car Make', validators=[DataRequired()])
    car_model = StringField('Car Model', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(1900, datetime.now().year)])
    image = StringField('Image URL', validators=[DataRequired(), Length(max=255), URL()])
    dealer_id = IntegerField('Dealer ID', validators=[DataRequired()])

class DealerForm(Form):
    company_name = StringField('Company Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])


class BuyerForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])


class OrderForm(Form):
    car_id = IntegerField('Car ID', validators=[DataRequired()])
    car_price = FloatField('Car Price', validators=[DataRequired()])
    buyer_id = IntegerField('Buyer ID', validators=[DataRequired()])

class Cars(Resource):
    def get(self):
        cars = Car.query.all()
        return jsonify([car.serialize() for car in cars])

    def post(self):
        form = CarForm(request.form)
        if form.validate():
            car = Car(
                car_make=form.car_make.data,
                car_model=form.car_model.data,
                price=form.price.data,
                year=form.year.data,
                image=form.image.data,
                dealer_id=form.dealer_id.data
            )
            db.session.add(car)
            db.session.commit()
            return jsonify({'message': 'Car created successfully', 'car': car.serialize()}), 201
        return jsonify({'error': 'Invalid input', 'errors': form.errors}), 400

api.add_resource(Cars, '/cars')

class CarsById(Resource):
    def get(self, car_id):
        car = Car.query.get(car_id)
        if car:
            return jsonify(car.serialize())
        return jsonify({'error': 'Car not found'}), 404

    def patch(self, car_id):
        car = Car.query.get(car_id)
        if car:
            form = CarForm(request.form)
            if form.validate():
                car.car_make = form.car_make.data
                car.car_model = form.car_model.data
                car.price = form.price.data
                car.year = form.year.data
                car.image = form.image.data
                car.dealer_id = form.dealer_id.data
                db.session.commit()
                return jsonify({'message': 'Car updated successfully', 'car': car.serialize()})
            return jsonify({'error': 'Invalid input', 'errors': form.errors}), 400
        return jsonify({'error': 'Car not found'}), 404
    
    def delete(self, car_id):
        car = Car.query.get(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()
            return jsonify({'message': 'Car deleted successfully'})
        return jsonify({'error': 'Car not found'}), 404
    
api.add_resource(CarsById, '/cars/<int:car_id>')

class Dealers(Resource):
    def get(self):
        dealers = Dealer.query.all()
        return jsonify([dealer.serialize() for dealer in dealers])

    def post(self):
        form = DealerForm(request.form)
        if form.validate():
            dealer = Dealer(
                company_name=form.company_name.data,
                email=form.email.data,
                phone_number=form.phone_number.data
            )
            db.session.add(dealer)
            db.session.commit()
            return jsonify({'message': 'Dealer created successfully', 'dealer': dealer.serialize()}), 201
        return jsonify({'error': 'Invalid input', 'errors': form.errors}), 400
    
api.add_resource(Dealers, '/dealers')
    
class DealersById(Resource):
    def get(self, dealer_id):
        dealer = Dealer.query.get(dealer_id)
        if dealer:
            return jsonify(dealer.serialize())
        return jsonify({'error': 'Dealer not found'}), 404

    def delete(self, dealer_id):
        dealer = Dealer.query.get(dealer_id)
        if dealer:
            db.session.delete(dealer)
            db.session.commit()
            return jsonify({'message': 'Dealer deleted successfully'})
        return jsonify({'error': 'Dealer not found'}), 404
    
api.add_resource(DealersById, '/dealers/<int:dealer_id>')

class Buyers(Resource):
    def get(self):
        buyers = Buyer.query.all()
        return jsonify([buyer.serialize() for buyer in buyers])

    def post(self):
        form = BuyerForm(request.form)
        if form.validate():
            buyer = Buyer(
                name=form.name.data,
                email=form.email.data,
                phone_number=form.phone_number.data
            )
            db.session.add(buyer)
            db.session.commit()
            return jsonify({'message': 'Buyer created successfully', 'buyer': buyer.serialize()}), 201
        return jsonify({'error': 'Invalid input', 'errors': form.errors}), 400
    
api.add_resource(Buyers, '/buyers')

class BuyersById(Resource):
    def get(self, buyer_id):
        buyer = Buyer.query.get(buyer_id)
        if buyer:
            return jsonify(buyer.serialize())
        return jsonify({'error': 'Buyer not found'}), 404
    
    def delete(self, buyer_id):
        buyer = Buyer.query.get(buyer_id)
        if buyer:
            db.session.delete(buyer)
            db.session.commit()
            return jsonify({'message': 'Buyer deleted successfully'})
        return jsonify({'error': 'Buyer not found'}), 404
    
api.add_resource(BuyersById, '/buyers/<int:buyer_id>')

# api.add_resource(Orders, '/orders')
# api.add_resource(OrdersById, '/orders/<int:order_id>')

=======


>>>>>>> 75a7db0 (models)
if __name__ == '__main__':
    app.run(port=5555)
