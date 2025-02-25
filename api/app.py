from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from pydantic import BaseModel
from utils import init_db
from typing import List, Dict, Any
import os
 
MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@172.20.0.6:27017/")
DB_NAME = "bike_shop_db"
# init db with false data
init_db(MONGO_URI)
# Initialiser FastAPI
app = FastAPI(title="Bike Shop API", description="API de vente en ligne avec FastAPI")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connexion à MongoDB
def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    try:
        yield db
    finally:
        client.close()

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
async def home():
    return {"message": "Bienvenue sur l'API de Bike Shop"}

# Route pour récupérer tous les produits
@app.get("/products", response_model=list[Product])
async def get_products(db=Depends(get_db)):
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")
    products = list(db['products'].find({}))
    if not products:
        raise HTTPException(status_code=501, detail="Produit non trouvé")
    
    return products

# Route pour récupérer un produit par son ID
@app.get("/products/{product_handle}", response_model=Product)
async def get_product_by_id(product_handle: str, db=Depends(get_db)):
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")
    product = db['products'].find_one({"handle": product_handle})
    if not product:
        raise HTTPException(status_code=501, detail="Produit non trouvé")
    
    return product

# Route pour récupérer les informations de contact
@app.get("/contact")
async def get_contact(db=Depends(get_db)):
    if db is None:
        raise HTTPException(status_code=500, detail="Connexion à MongoDB échouée")
    contact_info = db['contact_info'].find_one({}, {"_id": 0})  # Exclure `_id`
    if not contact_info:
        raise HTTPException(status_code=501, detail="Informations de contact non trouvées")
    
    return contact_info
