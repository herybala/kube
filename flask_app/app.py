from flask import Flask, render_template, request
from pymongo import MongoClient
from utils import init_db

app = Flask(__name__)

# Connexion à MongoDB
init_db()
client = MongoClient('mongodb://admin:password@172.20.0.6:27017/')  # Remplacez par l'URI de votre MongoDB si nécessaire
db = client['bike_shop_db']
products_collection = db['products']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    # Récupérer les produits depuis la base de données
    products = list(products_collection.find())
    return render_template('products.html', products=products)

@app.route('/contact')
def contact_page():
    # Récupérer les données de contact depuis la base de données
    contact_info = db['contact_info'].find_one({}, {'_id': 0})  # Exclure le champ `_id`
    return render_template('contact.html', contact_info=contact_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
