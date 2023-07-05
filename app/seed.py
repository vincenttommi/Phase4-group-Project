from random import choice as rc
from faker import Faker
from app import app, db
from models import Car, Dealer, Buyer, Order

fake = Faker()

# List of car makes and models
car_makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai',
             'Kia', 'Subaru', 'Mazda', 'Lexus', 'Jeep', 'GMC', 'Ram', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai',
             'Kia', 'Subaru', 'Mazda', 'Lexus', 'Jeep', 'GMC', 'Ram', 'Ford', 'Chevrolet', 'Nissan', 'Toyota', 'Honda',
             'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Hyundai', 'Kia', 'Subaru', 'Mazda', 'Lexus', 'Jeep', 'GMC',
             'Ram', 'Ford', 'Chevrolet', 'Nissan', 'Toyota', 'Honda']

car_models = ['Camry', 'Civic', 'Mustang', 'Silverado', 'Altima', '3 Series', 'C-Class', 'A4', 'Golf', 'Elantra',
              'Soul', 'Outback', 'Mazda3', 'RX', 'Wrangler', 'Sierra', '1500', 'Explorer', 'Tahoe', 'Rogue', 'RAV4',
              'CR-V', '5 Series', 'E-Class', 'Q5', 'Passat', 'Tucson', 'Sportage', 'Forester', 'CX-5', 'ES',
              'Grand Cherokee', 'Acadia', '2500', 'F-150', 'Equinox', 'Pathfinder', 'Highlander', 'Pilot', 'X5',
              'GLE', 'Q7', 'Tiguan', 'Santa Fe', 'Sorento', 'Impreza', 'Mazda6', 'NX', 'Cherokee', 'Terrain']

def generate_phone_number():
    country_code = "(254)"
    random_numbers = fake.random_int(min=100, max=999)
    formatted_number = f"{country_code}{random_numbers:03}"
    formatted_number += "-".join([f"{fake.random_int(min=100, max=999):03}" for _ in range(3)])
    return formatted_number

with app.app_context():

    # Drop existing tables and recreate them
    db.drop_all()
    db.create_all()

    # Create dealers
    dealers = []
    for _ in range(15):
        dealer = Dealer(
            company_name=fake.company(),
            email=fake.email(),
            phone_number=generate_phone_number()
        )
        dealers.append(dealer)
        db.session.add(dealer)
    db.session.commit()
    # Create cars
    cars = []
    for i in range(50):
        dealer = fake.random_element(dealers)  # Assign a random dealer to the car
        car_make = car_makes[i]  # Assign the car make based on the index
        car_model = car_models[i]  # Assign the car model based on the index
        price = fake.random_int(min=100000, max=2000000)
        year = fake.random_int(min=2012, max=2023)  # Generate year between 2012 and 2023
        image = fake.image_url()
        car = Car(
            car_make=car_make,
            car_model=car_model,
            price=price,
            year=year,
            image=image,
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
                phone_number=generate_phone_number(),
                password=fake.password()
            )
            buyers.append(buyer)
            db.session.add(buyer)
    db.session.commit()

    # Create orders
    orders = []
    for _ in range(50):
        buyer = fake.random_element(buyers)  # Randomly select a buyer from the list
        car = fake.random_element(cars)  # Randomly select a car from the list
        order = Order(
            car=car,
            car_price=car.price,
            buyer_id=buyer.id,
            order_date=fake.date_this_decade()
        )
        orders.append(order)
        db.session.add(order)
    db.session.commit()