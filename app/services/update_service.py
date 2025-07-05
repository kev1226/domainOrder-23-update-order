import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Conexión Mongo
mongo_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

client = MongoClient(mongo_uri)
orders = client[db_name]["orders"]


# Servicio de actualización
async def update_order_status(order_id: str, email: str, roles: list):
    order = orders.find_one({"_id": ObjectId(order_id)})

    if not order:
        raise Exception("Orden no encontrada")

    if order["user"]["email"] != email and "admin" not in roles:
        raise Exception("No tienes permisos para actualizar esta orden")

    if order["status"] != "PENDIENTE_DE_PAGO":
        raise Exception("Solo se pueden actualizar órdenes pendientes de pago")

    orders.update_one({"_id": ObjectId(order_id)}, {"$set": {"status": "PAGADA"}})

    return {"id": order_id, "status": "PAGADA"}
