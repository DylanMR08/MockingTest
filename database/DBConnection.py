import os
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv as le
le(".env")

class DBConnection:
    @classmethod
    def getConnection(cls):
        try:
            client = MongoClient(f"mongodb://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/")
            db = client.get_database(os.getenv('DB_NAME'))
            return db
        except Exception as e:
            print(f"Error de conexión a la base de datos: {str(e)}")
            raise

    @classmethod
    def insert(cls, collection, document: dict):
        result: str = ""
        try:
            document.pop("id")
            db = cls.getConnection()
            collection = db.get_collection(collection)
            result = collection.insert_one(document).inserted_id
        except Exception as e:
            print(f"Error al insertar el documento: {str(e)}")
            raise
        finally:
            db.client.close()
            return result

    @classmethod
    def delete(cls, collection, id):
        result: bool = False
        try:
            db = cls.getConnection()
            collection = db.get_collection(collection)
            response = collection.delete_one({"_id": ObjectId(id)})
            result = True if response.deleted_count == 1 else result
        except Exception as e:
            print(f"Error al eliminar documentos: {str(e)}")
            raise
        finally:
            db.client.close()
            return result

    @classmethod
    def update(cls, collection, id,document: dict):
        result: bool = False
        try:
            document.pop("id")
            db = cls.getConnection()
            collection = db.get_collection(collection)
            response = collection.update_one({"_id": ObjectId(id)}, {"$set": document})
            result = True if response.modified_count == 1 else result
        except Exception as e:
            print(f"Error al modificar documentos: {str(e)}")
            raise
        finally:
            db.client.close()
            return result

    @classmethod
    def findOne(cls, collection, id):
        result: dict | None = {}
        try:
            db = cls.getConnection()
            collection = db.get_collection(collection)
            result = collection.find_one({"_id": ObjectId(id)})
        except Exception as e:
            print(f"Error al obtener los documentos: {str(e)}")
            raise
        finally:
            db.client.close()
            return result

    @classmethod
    def getAll(cls, collection, create):
        result: list = []
        try:
            db = cls.getConnection()
            collection = db.get_collection(collection)
            result = list(
                map(lambda x: create(x), collection.find())
            )
        except Exception as e:
            print(f"Error al obtener los documentos: {str(e)}")
            raise
        finally:
            db.client.close()
            return result