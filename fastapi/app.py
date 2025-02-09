from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from utils import init_db
from typing import List, Dict, Any
import os
 
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@172.20.0.6:27017/")
# init db with false data
init_db(MONGO_URI)
# Initialiser FastAPI
app = FastAPI(title="Bike Shop API", description="API de vente en ligne avec FastAPI")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connexion à MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client['bike_shop_db']
    print("✅ Connexion réussie à MongoDB")
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
    db = None
    
# Configurer Jinja2 pour les templates
templates = Jinja2Templates(directory="templates")

# Modèle Pydantic pour la validation des produits
# class Product(BaseModel):
#     name: str
#     price: float
#     category: str
#     stock: int
#     image_url: str

class ImageNode(BaseModel):
    altText: str
    height: int
    width: int
    id: str
    originalSrc: str

class ImageEdge(BaseModel):
    node: ImageNode

class VariantNode(BaseModel):
    id: str
    price: float
    title: str

class VariantEdge(BaseModel):
    node: VariantNode

class Product(BaseModel):
    _id: str
    description: str
    handle: str
    title: str
    images: Dict[str, List[ImageEdge]]
    variants: Dict[str, List[VariantEdge]]


# Route d'accueil
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Bike Shop"}

# Route pour récupérer tous les produits
@app.get("/products", response_model=list[Product])
def get_products():
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")

    products = list(db['products'].find({}))
    return products

# Route pour récupérer un produit par son ID
@app.get("/products/{product_handle}", response_model=Product)
def get_product_by_id(product_handle: str):
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")

    # Vérifier si l'ID est valide
    # if not ObjectId.is_valid(product_id):
    #     raise HTTPException(status_code=400, detail="ID du produit invalide")

    product = db['products'].find_one({"handle": product_handle})
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    
    return product

# Route pour récupérer les informations de contact
@app.get("/contact")
def get_contact():
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")

    contact_info = db['contact_info'].find_one({}, {"_id": 0})  # Exclure `_id`
    if not contact_info:
        raise HTTPException(status_code=404, detail="Informations de contact non trouvées")
    return contact_info
