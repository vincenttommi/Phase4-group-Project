from random import choice as rc
from faker import Faker

from app import app, db
from models import Car, Dealer, Buyer, Order

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Rest of your code...

    dealers = []
    cars = []
    buyers = []

    for _ in range(50):
        dealer = Dealer(
            company_name=fake.company(),
            email=fake.email(),
            phone_number=fake.phone_number()
        )
        dealers.append(dealer)
        db.session.add(dealer)

    for _ in range(50):
        car = Car(
            car_make=fake.name(),
            car_model=fake.name(),
            price=fake.random_int(min=1000, max=50000),
            year=fake.year(),
            image=fake.image_url(),
            dealer=rc(dealers)  # Assign a random dealer to the car
        )
        cars.append(car)
        db.session.add(car)

    for _ in range(50):
        buyer = Buyer(
            name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number()
        )
        buyers.append(buyer)
        db.session.add(buyer)

Orders = []

for _ in range(50):
    buyer = rc(buyers)  # Randomly select a buyer from the list
    order = Order(
        car=rc(cars),  # Randomly select a car from the list
        car_price=fake.random_int(min=1000, max=50000),
        buyer_id=buyer.id,  # Use the ID of the buyer
        order_date=fake.date_this_decade()
    )
    Orders.append(order)
    db.session.add(order)

    db.session.commit()
