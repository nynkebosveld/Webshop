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


def create_tables():
    with db:
        db.drop_tables([User, Product, Purchase])
        db.create_tables([User, Product, Purchase])


def populate_tables():
    i = 0
    while i < 10:
        tags = 'tag ' + str(i)
        User.create(username='test', adress='test', billingInfo='test')
        Product.create(name='test', price=1.0, description='test', stock=1, owner=1, tags=tags)
        i += 1
    print('Tables populated!')


create_tables()
