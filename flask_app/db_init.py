from pymongo import MongoClient

# Connexion à MongoDB
# client = MongoClient('mongodb://admin:password@localhost:27017/')
client = MongoClient(
    'mongodb://admin:password@172.20.0.6:27017'
)
db = client['bike_shop_db']
products_collection = db['products']
contact_info_collection = db['contact_info']

# Données initiales
products = [
    {"name": "Vélo de route", "price": 800, "category": "Vélos", "stock": 10, "image_url": "/static/images/velo_route.jpg"},
    {"name": "VTT", "price": 600, "category": "Vélos", "stock": 15, "image_url": "/static/images/vtt.jpg"},
    {"name": "Vélo électrique", "price": 1200, "category": "Vélos", "stock": 5, "image_url": "/static/images/velo_electrique.jpg"}
]

# Insérer les données si elles n'existent pas déjà
if products_collection.count_documents({}) == 0:
    products_collection.insert_many(products)
    print("Produits insérés dans la base de données.")
else:
    print("La base de données contient déjà des produits.")

if contact_info_collection.count_documents({}) == 0:
    contact_info = {
        "address": "CESI Mauguio",
        "phone": "+33 3 33 33 33 33",
        "email": "contact@bike-shop.fr",
        "opening_hours": {
            "lundi": "9h - 18h",
            "mardi": "9h - 18h",
            "mercredi": "9h - 18h",
            "jeudi": "9h - 18h",
            "vendredi": "9h - 18h",
            "samedi": "10h - 16h",
            "dimanche": "Fermé"
        }
    }
    contact_info_collection.insert_one(contact_info)
    print("Données de contact insérées dans la base de données.")
else:
    print("Les données de contact existent déjà.")
