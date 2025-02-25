from pymongo import MongoClient
from bson import ObjectId

def init_db(MONGO_URI):
    try:
        client = MongoClient(MONGO_URI)
        db = client['bike_shop_db']
        print("✅ Connexion réussie à MongoDB")
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")
        db = None
    db = client['bike_shop_db']
    products_collection = db['products']
    contact_info_collection = db['contact_info']

    # Données initiales
    # products = [
    #     {"id": "0001", "name": "Vélo de route", "price": 800, "category": "Vélos", "stock": 10, "image_url": "http://localhost/static/images/velo_route.jpg"},
    #     {"id": "0002", "name": "VTT", "price": 600, "category": "Vélos", "stock": 15, "image_url": "http://localhost/static/images/vtt.jpg"},
    #     {"id": "0003", "name": "Vélo électrique", "price": 1200, "category": "Vélos", "stock": 5, "image_url": "http://localhost/static/images/velo_electrique.jpg"}
    #     ]
    products = [
                {
                    "description": "Vélo de route, un vélo parfait pour la route.",
                    "handle": "velo-de-route",
                    "title": "Vélo de route",
                    "images": {
                        "edges": [
                        {
                            "node": {
                            "altText": "vélo de route",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-1",
                            "originalSrc": "http://localhost/static/images/velo_route.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo de route",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-2",
                            "originalSrc": "http://localhost/static/images/velo_route.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo de route",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-3",
                            "originalSrc": "http://localhost/static/images/velo_route.jpg"
                            }
                        }
                        ]
                    },
                    "variants": {
                        "edges": [
                        {
                            "node": {
                            "id": "variant-1",
                            "price": "800",
                            "title": "S"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-2",
                            "price": "820",
                            "title": "M"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-3",
                            "price": "830",
                            "title": "L"
                            }
                        }
                        ]
                    }
                },
                {
                    "description": "Vélo tout terrain",
                    "handle": "vtt",
                    "title": "Vélo tout terrain",
                    "images": {
                        "edges": [
                        {
                            "node": {
                            "altText": "vélo tout terrain",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-1",
                            "originalSrc": "http://localhost/static/images/vtt.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo tout terrain",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-2",
                            "originalSrc": "http://localhost/static/images/vtt.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo tout terrain",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-3",
                            "originalSrc": "http://localhost/static/images/vtt.jpg"
                            }
                        }
                        ]
                    },
                    "variants": {
                        "edges": [
                        {
                            "node": {
                            "id": "variant-1",
                            "price": "800",
                            "title": "S"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-2",
                            "price": "820",
                            "title": "M"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-3",
                            "price": "830",
                            "title": "L"
                            }
                        }
                        ]
                    }
                },
                {
                    "description": "Vélo électrique",
                    "handle": "velo_electrique",
                    "title": "Vélo électrique",
                    "images": {
                        "edges": [
                        {
                            "node": {
                            "altText": "vélo électrique",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-1",
                            "originalSrc": "http://localhost/static/images/velo_electrique.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo électrique",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-2",
                            "originalSrc": "http://localhost/static/images/velo_electrique.jpg"
                            }
                        },
                        {
                            "node": {
                            "altText": "vélo électrique",
                            "height": 1000,
                            "width": 1000,
                            "id": "image-3",
                            "originalSrc": "http://localhost/static/images/velo_electrique.jpg"
                            }
                        }
                        ]
                    },
                    "variants": {
                        "edges": [
                        {
                            "node": {
                            "id": "variant-1",
                            "price": "800",
                            "title": "S"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-2",
                            "price": "820",
                            "title": "M"
                            }
                        },
                        {
                            "node": {
                            "id": "variant-3",
                            "price": "830",
                            "title": "L"
                            }
                        }
                        ]
                    }
                }
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