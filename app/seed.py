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

image_url = ['https://images.unsplash.com/photo-1664287721774-13da4b108b18?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80',
             'https://images.unsplash.com/photo-1605816988069-b11383b50717?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=888&q=80',
             'https://images.unsplash.com/photo-1547744152-14d985cb937f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Zm9yZCUyMG11c3Rhbmd8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60',
             'https://images.unsplash.com/photo-1645830122484-e0aa9955456a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=415&q=80',
             'https://images.unsplash.com/photo-1581540222194-0def2dda95b8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://images.unsplash.com/photo-1613027570801-5d2fe8f5e15d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80',
             'https://images.unsplash.com/photo-1653674022994-f9081eec1a53?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80',
             'https://images.unsplash.com/photo-1596564239685-09d2e88e1bb9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=465&q=80',
             'https://images.unsplash.com/photo-1571388429034-9ce53dbf0047?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://images.unsplash.com/photo-1671691279941-71773546ab76?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=580&q=80',
             'https://images.unsplash.com/photo-1592805723127-004b174a1798?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://images.unsplash.com/photo-1652047963668-42d09fd3ae71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=473&q=80',
             'https://images.unsplash.com/photo-1684734184331-439ade2d8f84?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=387&q=80',
             'https://images.unsplash.com/photo-1664427356346-c31b46248e71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://images.unsplash.com/photo-1579044587961-5e370f6080bc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://images.unsplash.com/photo-1657145076873-fbee01c714db?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80',
             'https://di-uploads-pod34.dealerinspire.com/prestigechryslerjeepdodge/uploads/2021/12/2022-Ram-Rebel-GT-1.jpg',
             'https://www.explorervan.com/wp-content/uploads/2021/05/Explorer_Mercedes_Shop_0049.jpeg',
             'https://images.dealer.com/ddc/vehicles/2023/Audi/Q3/SUV/trim_45_S_line_Premium_4c81a0/color/Glacier%20White%20Metallic-2Y2Y-229%2C230%2C229-640-en_US.jpg?impolicy=downsize_bkpt&imdensity=1&w=520',
             'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80',
             'https://cdn.jdpower.com/JDP_2022%20Hyundai%20Tucson%20XRT%20Silver%20Front%20Quarter%20View.jpg',
             'https://www.motorbiscuit.com/wp-content/uploads/2022/01/Kia-Sportage-3.jpg?w=1200',
             'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/2022_Subaru_WRX_GT_in_Ceramic_White%2C_front_left_%28NYIAS_2022%29.jpg/800px-2022_Subaru_WRX_GT_in_Ceramic_White%2C_front_left_%28NYIAS_2022%29.jpg',
             'https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1620994232/autoexpress/2021/05/Mazda%203%20e-SkyActiv%20X-6.jpg',
             'https://dealerimages.dealereprocess.com/image/upload/1780172.jpg',
             'https://images.drive.com.au/driveau/image/upload/c_fill,f_auto,g_auto,h_674,q_auto:eco,w_1200/v1/cms/uploads/AujVb6TaGNkWf9LPYkwG',
             'https://dealerimages.dealereprocess.com/image/upload/1919225.jpg',
             'https://hips.hearstapps.com/hmg-prod/images/rm022-429fnjcm5ijkgvrntnhqaas5eh699ns-1632407498.jpg',
             'https://upload.wikimedia.org/wikipedia/commons/8/89/2015_Ford_Everest_Titanium_%28New_Zealand%29.jpg',
             'https://static.bangkokpost.com/media/content/20190909/3320874.jpg',
             'https://autoskenya.s3.amazonaws.com/uploads/post/featured_image/62/nissan_x_trail.jpg',
             'https://toyota-cms-media.s3.amazonaws.com/wp-content/uploads/2023/02/2024_Toyota_GrandHighlander_StormCloud_001-1500x1000.jpg',
             'https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fpeterlyon%2Ffiles%2F2018%2F09%2FCR-V_1.jpg',
             'https://cdn.autowereld.nl/I588844578/1280x0/bmw-2-5-2-8-3-0-2500-orig-ned-e3-sedan.jpg',
             'https://editorial.pxcrush.net/carsales/general/editorial/mercedes-benz-x-class-013-q4iw.jpg?width=1024&height=682',
             'https://revistacarro.com.br/wp-content/uploads/2021/05/Audi-RS-e-tron-GT_2-1080x675.jpg',
             'https://i.ytimg.com/vi/D3LgVwznfb4/maxresdefault.jpg',
             'https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/segment_review/hero_image/2022-hyundai-tucson-highlander-grey-suv-richard-berry-1001x565-%281%29.jpg',
             'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/17761-2022-sorento-phev-2-1661538352.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=640:*',
             'https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/subaru-xv-20is-tr-2018-%2814%29.jpg',
             'https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/2022-mazda-cx-5-suv-red-1001x565-%281%29.jpg',
             'https://carsguide-res.cloudinary.com/image/upload/f_auto%2Cfl_lossy%2Cq_auto%2Ct_default/v1/editorial/story/hero_image/2020-Lexus-RX300-SUV-silver-Richard-Berry-1001x565p-%281%29.jpg',
             'https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cdni.autocarindia.com/ExtraImages/20220204040930_Jeep_Commander_2.jpg&w=700&q=90&c=1',
             'https://carbuyerlabs.com/wp-content/uploads/2019/04/2019-GMC-terrain-vs-2019-Hyundai-Santa-Fe-Terrain-Denali-Black.jpg',
             'https://i.pinimg.com/originals/33/42/e3/3342e394c1e1a4ff0b70d98de9f8db78.jpg',
             'https://imgd.aeplcdn.com/0x0/n/cw/ec/35583/aspire-exterior-right-front-three-quarter-2.jpeg',
             'https://hips.hearstapps.com/hmg-prod/images/2018-chevrolet-impala-106-1529679402.jpg?crop=0.842xw:0.806xh;0.0374xw,0.0639xh&resize=1200:*',
             'https://inv.assets.sincrod.com/ChromeColorMatch/us/WHITE_cc_2023NIC060012_01_1280_QAC.jpg',
             'https://vehiclephotos.b-cdn.net/photos/vehicles/243326/4161313-large.jpg',
             'https://hips.hearstapps.com/hmg-prod/images/10best-trucks-suvs-2023-honda-crv-113-1673298616.jpg?crop=0.634xw:0.714xh;0.181xw,0.230xh&resize=640:*']


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
        image = image_url[i]
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