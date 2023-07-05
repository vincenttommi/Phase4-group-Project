from random import choice as rc
from faker import Faker
from app import app, db
from models import Car, Dealer, Buyer, Order
fake = Faker()
with app.app_context():
    # Drop existing tables and recreate them
    db.drop_all()
    db.create_all()
    # Create dealers
    dealers = []
    for _ in range(50):
        dealer = Dealer(
            company_name=fake.company(),
            email=fake.email(),
            phone_number=fake.phone_number()
        )
        dealers.append(dealer)
        db.session.add(dealer)
    db.session.commit()
    # Create cars
    cars = []
    for _ in range(50):
        dealer = rc(dealers)  # Assign a random dealer to the car
        car = Car(
            car_make=fake.name(),
            car_model=fake.name(),
            price=fake.random_int(min=1000, max=50000),
            year=fake.year(),
            image=fake.image_url(),
            dealer=dealer
        )
        cars.append(car)
        db.session.add(car)
    db.session.commit()
    # Create buyers
    buyers = []
    for _ in range(50):
        buyer = Buyer(
            name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            password=fake.password()
        )
        buyers.append(buyer)
        db.session.add(buyer)
    db.session.commit()
    # Create orders
    orders = []
    for _ in range(50):
        buyer = rc(buyers)  # Randomly select a buyer from the list
        car = rc(cars)  # Randomly select a car from the list
        order = Order(
            car=car,
            car_price=car.price,
            buyer_id=buyer.id,
            order_date=fake.date_this_decade()
        )
        orders.append(order)
        db.session.add(order)
    db.session.commit()