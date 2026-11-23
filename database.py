from pymongo import MongoClient
import certifi

MONGO_URI="mongodb+srv://benjaminsoto_db_user:xyHouqNgNIqYnIAN@cluster0.6hytjco.mongodb.net/"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db=client["dbb_products_app"]
    except ConnectionError:
        print ('Error de conexion con la bdd')
    return db
