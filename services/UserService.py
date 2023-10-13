from database.DBConnection import DBConnection
from models.User import User


class UserService:
    
    def __init__(self) -> None:
        self.db = DBConnection()
    
    def store(self, user: User):
        if self.db.insert("tbUsuarios", user.model_dump()) != "":
            return True
        return False

    def update(cls, user: User):
        return DBConnection.update("tbUsuarios", user.id, user.model_dump())

    def getUser(self, id: str):
        result = self.db.findOne("tbUsuarios", id)
        if result is not None:
            result = self.db.createUser(result)
        return result

    def getAll(self):
        return self.db.getAll("tbUsuarios", self.createUser)

    def delete(self, id: str):
        if self.db.delete("tbUsuarios", id):
            return True
        return False
    
    def createUser(self, user):
        return User(
            id=str(user["_id"]),
            name=user["name"],
            lastName=user["lastName"],
            telephone=user["telephone"]
        ).model_dump_json()