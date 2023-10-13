from unittest import TestCase, main
from unittest.mock import Mock
from services.UserService import UserService
from models.User import User


class TestUserServiceMock(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.dbConnectionMock = Mock()
        cls.dbConnectionMock.insert.return_value = "fwefwfwwe"
        cls.dbConnectionMock.update.return_value = True
        cls.dbConnectionMock.findOne.return_value = {
            "_id": "8938434rdfshfiweuwf",
            "name": "John",
            "lastName": "Doe",
            "telephone": "67689090"
        }
        cls.dbConnectionMock.getAll.return_value = [
            {"id": "234224sfefewfwf", "name": "John", "lastName": "Doe", "telephone": "67689090"}
        ]
        cls.dbConnectionMock.delete.return_value = True

    @classmethod
    def tearDownClass(cls):
        cls.dbConnectionMock = None

    def setUp(self):
        self.userServiceMock = UserService()
        self.userServiceMock.db = self.dbConnectionMock
        data = {"name": "John", "lastName": "Doe", "telephone": "67689090"}
        self.user = User(**data)
        self.service = UserService()

    def test_get_all_mock(self):
        expectedResult = [{"id": "234224sfefewfwf","name": "John", "lastName": "Doe", "telephone": "67689090"}]
        result = self.userServiceMock.getAll()
        self.assertListEqual(result, expectedResult, msg="El resultado no es igual al esperado")

    def test_insert_mock(self):
        result = self.userServiceMock.store(self.user)
        self.assertIsInstance(self.user, User, msg=f"No es instancia de la clase User")
        self.assertTrue(result, msg="Error al insertar el usuario")
    
    def test_real_insert(self):
        result = self.service.store(self.user)
        self.assertTrue(result, msg="Error al insertar el usuario")
        
    def test_real_delete(self):
        id = "65288964605e2845255bd3e0"
        result = self.service.delete(id)
        self.assertEqual(result, True)