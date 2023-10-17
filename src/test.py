# import csv

# BRANDNAME_CHOICES = [
#     ('Chevrolet', 'Chevrolet'), ('Force', 'Force'), ('Renault', 'Renault'),
#     ('Jeep', 'Jeep'), ('Mitsubishi', 'Mitsubishi'), ('Ford', 'Ford'),
#     ('Mercedes', 'Mercedes'), ('BMW', 'BMW'), ('Fiat', 'Fiat'),
#     ('Audi', 'Audi'), ('Datsun', 'Datsun'), ('Mini', 'Mini'),
#     ('Nissan', 'Nissan'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'),
#     ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Jaguar', 'Jaguar'),
#     ('Skoda', 'Skoda'), ('Suzuki', 'Suzuki'), ('Mahindra', 'Mahindra'),
#     ('Maruti', 'Maruti'), ('Tata', 'Tata'), ('Hindustan', 'Hindustan'),
#     ('Toyota', 'Toyota'), ('Land', 'Land')
# ]

# # Define the CSV file name
# csv_file = "brandnames.csv"

# # Write the data to the CSV file
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(BRANDNAME_CHOICES)

# print(f"Data has been written to {csv_file}")
import csv

# Your car name choices
CARNAME_CHOICES = [
    'Kwid RXT Opt', 'A3 Cabriolet 40 TFSI', 'Elantra 1.8 S', 'Etios Liva G', 'City SV', 'Laura',
    'Suzuki Zen LXi BSII', 'i20 Asta 1.2', 'Scorpio VLX 4WD Airbag', 'Santro Xing XL eRLX Euro III',
    'Suzuki Omni Limited Edition', 'Scorpio W Turbo 2.6DX 9 Seater', 'Figo Petrol LXI',
    'City 1.5 S Inspire', 'City 1.5 S MT', 'Zest Quadrajet 1.3', 'Verna 1.6 CRDI SX Plus AT',
    'Indigo Marina LS', 'Bolero DI BSII', 'Suzuki Wagon R LXi BS III', 'Go Plus', 'Suzuki Dzire',
    'Grand i10 Asta 1.2 Kappa VTVT', 'Scorpio S4', 'Corolla', '7 Series 740Li Sedan',
    'Corolla Altis VL AT Petrol', 'Indigo CS eLX BS IV', 'Sumo Gold LX BS IV',
    'Vento Highline Plus 1.5 Diesel AT', 'S80 Summum D4', 'i20 Active', 'Scorpio', 'Jazz VX MT',
    'i10', 'Tiago Revotron XM', 'Sumo Victa EX 10 by 7', 'Scorpio VLX 2WD BS IV', 'City ZX VTEC',
    'A4 1.8 TFSI Multitronic Premium Plus', 'Figo Diesel EXI', 'i20 Active 1.4L SX O', 'Suzuki Ertiga',
    'Innova 2.5 V 7 STR', 'Bolero SLE BS IV', 'Nano', 'Verna 1.6 SX VTVT AT', 'Jeep MM 550 XDB',
    'Scorpio Vlx BSIV', 'Ikon 1.3 Flair Josh 100', 'Xylo D2 BS IV', 'Suzuki S Cross Sigma 1.3',
    'Fabia', 'Octavia Classic 1.9 TDI MT', 'Elite i20', 'Grand i10 Asta 1.1 CRDi', 'Motors One SUV',
    'i20 Magna 1.2', 'Eon', 'XE XE Portfolio', 'Scorpio SLX', 'GO T O', 'Beat LT Petrol', 'Spark',
    'Suzuki Dzire VDI', 'Scala RxL Diesel', 'Q5 2.0 TDI quattro Premium Plus',
    'Suzuki Swift Dzire Tour VDi', 'XUV500 W6', 'Suzuki Swift', 'Suzuki Wagon R 1.0', 'TUV300 T8',
    'Suzuki Vitara Brezza LDi O', 'Corolla Altis Diesel D4DG', 'Fabia 1.2L Diesel Ambiente',
    'Suzuki Ertiga Vxi', '5 Series 520d Sedan', 'A4 2.0 TDI 177bhp Premium', 'i20 Magna', 'Bolt XM Petrol',
    'Polo Highline1.2L P', 'Suzuki Eeco 7 STR', 'Motors Ambassador Classic Mark 4 â€“', 'i10 Sportz',
    'Suzuki Swift Vdi BSIII', 'Suzuki Wagon R VXi Minor', 'Innova 2.0 G 8 STR BS', 'i10 Magna 1.2',
    'Suzuki Maruti 800 Std', 'Innova 2.5 G BS III 8', 'Indigo CS GLS', 'XUV500 W8 AWD 2013',
    'Suzuki Swift Dzire Tour LXi', 'Suzuki Omni', 'Sumo Gold EX BS IV', 'Suzuki Alto 800 Vxi',
    'TUV300 T4 Plus', 'Beat PS Diesel', 'Beat LS Petrol', 'Terrano XL D Plus', 'Beat',
    'Suzuki Alto K10 VXi AMT', 'Spark LT 1.0 Airbag', 'Suzuki Ritz VDi', 'Suzuki Swift VXi 1.2 BS IV',
    'Scorpio 2.6 CRDe', 'Corolla Altis', 'Cooper S 1.6', 'Santro Xing XO eRLX Euro III',
    'Suzuki Zen Estilo LXI Green CNG', 'Polo', 'Figo', 'Suzuki Ertiga ZXi', 'Sunny',
    'Sumo Gold Select Variant', 'Indica V2 DLE BS III', 'Fiesta SXi 1.6 ABS', 'Figo Petrol Titanium',
    'Figo Petrol Titanium', 'Accent Executive Edition', 'Logan Diesel 1.5 DLS', 'Q3 2.0 TDI quattro Premium',
    'City ZX CVT', 'Amaze 1.2 S i VTEC', 'Suzuki SX4 ZXI MT', 'Suzuki Alto K10 VXi', 'Etios Liva', 'Creta',
    'Getz Prime 1.3 GVS', 'Indigo eCS LS CR4 BS IV', 'Suzuki Wagon R LXI BS IV', 'Cruze LTZ AT',
    'Benz A Class A 180 Sport', 'Scorpio SLE BS IV', 'Eon Magna Plus', 'Sail 1.2 LS', 'Suzuki Alto LX',
    'Fiesta', 'Spark LS 1.0', 'Suzuki Vitara Brezza', 'Indigo eCS LX CR4 BS IV', 'Manza Aqua Quadrajet',
    'Santro Xing XS', 'Verna', 'Accent GLE', '5 Series 530i', 'City ZX GXi', 'XF 2.2 Diesel Luxury',
    'Duster 85 PS RxE Diesel', 'Suzuki Ritz LDi', 'Suzuki Wagon R LX BS IV', 'Suzuki Ritz VXI',
    'Suzuki Alto 800 Lxi', 'Verna Fluidic 1.6 VTVT SX', 'EcoSport Trend 1.5 Ti VCT', 'i10 Era',
    'Suzuki A Star Lxi', 'Kwid RXT', 'Suzuki Zen Estilo', 'Endeavor 4x4 Thunder Plus',
    'Scala RxL Diesel Travelogue', 'Fortuner 3.0 4x2 MT', 'Suzuki Swift VXI BSIII', 'Nano GenX XMA',
    'Scorpio 2.6 SLX', 'i20 Sportz 1.4 CRDI', 'Cooper S', 'Santro', 'Duster 110 PS RxL Diesel',
    'Suzuki Zen VX', 'Santro AE GLS Audio', 'Indica V2 LS', 'Getz Prime 1.3 GLX', 'Bolero Power Plus SLE',
    'Getz', 'Suzuki Omni Select Variant', 'Redi GO T O', 'Ikon 1.6 Nxt', 'Tavera LS B3 10 Seats BSII',
    'Creta 1.6 SX Plus Petrol', 'Suzuki Maruti 800 AC', 'Suzuki Celerio VDi',
    'Benz GLA Class 200 CDI Sport', 'Duster 85 PS RxL Explore LE', 'Indigo LS', 'Indica V2 eLS',
    'Indigo CS LS DiCOR', 'Etios Liva GD', 'Ikon 1.3 CLXi NXt Finesse', 'Suzuki Swift Dzire Tour VXi',
    'Suzuki Alto 800 Lx', 'Accent GLX', 'Grand i10 Sportz 1.2 Kappa VTVT', 'Indigo eCS LX TDI BS III',
    'Amaze', 'City 1.5 V MT', 'Elite i20 Asta 1.4 CRDI', 'Jazz S MT', 'Indica V2 DLG', 'Petra ELX 1.2 PS',
    'Suzuki Alto 800 LXI CNG O', 'Indigo CS', 'Amaze 1.5 E i DTEC', 'Duster 85 PS RxL Diesel',
    'Brio V MT', 'Suzuki Eeco 5 STR WITH AC', 'Scorpio VLX 2.2 mHawk Airbag BSIV', 'Suzuki Ritz VXI ABS',
    'Logan', 'Manza ELAN Quadrajet', 'Verna Transform SX VTVT', 'i20 Magna O 1.2', 'i20 Magna'
]

# Specify the name of the CSV file
csv_file_name = 'carnames.csv'

# Write car names to the CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Car Names'])  # Write header
    for car_name in CARNAME_CHOICES:
        writer.writerow([car_name])

print(f'Car names have been written to {csv_file_name}')
