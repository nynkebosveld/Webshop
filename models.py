from peewee import *

db = SqliteDatabase('betsyWebshop.db')


class User(Model):
    userId = PrimaryKeyField()
    username = CharField()
    adress = CharField()
    billingInfo = CharField()

    class Meta:
        database = db


class Product(Model):
    productId = PrimaryKeyField()
    name = CharField()
    price = DoubleField()
    description = CharField()
    stock = IntegerField()
    owner = ForeignKeyField(User, backref='products')
    tags = CharField(unique=True)

    class Meta:
        database = db


class Purchase(Model):
    purchaseId = PrimaryKeyField()
    buyer = ForeignKeyField(User, backref='purchases')
    product = ForeignKeyField(Product, backref='purchases')
    quantity = IntegerField()

    class Meta:
        database = db
