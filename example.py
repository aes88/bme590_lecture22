from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590_lecture15")

class User(MongoModel):
	name = fields.CharField(primary_key=True)
	age = fields.


