from models import *

db = SqliteDatabase('betsyWebshop.db')


def searchProducts(searchString):
    products = set()
    products |= set(Product.select().where(Product.name.contains(searchString)))
    products |= set(Product.select().where(Product.description.contains(searchString)))
    return list(products)


def searchProductsByTag(tags):
    return Product.select().where(Product.tags.contains(tags))


def searchProductsByOwner(userid):
    return Product.select().where(Product.owner.contains(userid))


def addProduct(name, price, description, stock, owner, tags):
    Product.create(name=name, price=price, description=description, stock=stock, owner=owner, tags=tags)


def removeProduct(productid):
    Product.delete().where(Product.productId == productid).execute()


def updateStock(productid, newStock):
    Product.update(stock=newStock).where(Product.productId == productid)


def getStock(productid):
    return Product.select(Product.stock).where(Product.productId == productid)


def addPurchase(userid, productid, quantity):
    Purchase.create(buyer=userid, product=productid, quantity=quantity)
    newStock = int(getStock(productid)) - quantity
    updateStock(productid, newStock)


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


if __name__ == '__main__':
    create_tables()
    populate_tables()
    # searchProducts('test')
    # searchProductsByTag('test')
    # searchProductsByOwner(1)
    # addProduct('test', 1.0, 'test', 1, 1, 'test')
    # removeProduct(1)
