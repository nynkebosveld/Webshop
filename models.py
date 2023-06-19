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

    class Meta:
        database = db


class Tag(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class ProductTag(Model):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)


class Purchase(Model):
    purchaseId = PrimaryKeyField()
    buyer = ForeignKeyField(User, backref='purchases')
    product = ForeignKeyField(Product, backref='purchases')
    quantity = IntegerField()

    class Meta:
        database = db
