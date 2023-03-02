from models import *

db = SqliteDatabase('betsyWebshop.db')


def searchProducts(searchString):
    products = Product.select().where(Product.name.contains(searchString))
    products += Product.select().where(Product.description.contains(searchString))
    return products


def searchProductsByTag(tags):
    return Product.select().where(Product.tags.contains(tags))


def searchProductsByOwner(userid):
    return Product.select().where(Product.owner.contains(userid))


def addProduct(name, price, description, stock, owner, tags):
    Product.create(name=name, price=price, description=description, stock=stock, owner=owner, tags=tags)


def removeProduct(productid):
    Product.delete().where(Product.productId == productid)


def updateStock(productid, newStock):
    Product.update(stock=newStock).where(Product.productId == productid)

def addPurchase(userid, productid, quantity):
    Purchase.create(buyer=userid, product=productid, quantity=quantity)


if __name__ == '__main__':
    # create_tables()
    # populate_tables()
    searchProducts('test')
    searchProductsByTag('test')
    searchProductsByOwner(1)
    addProduct('test', 1.0, 'test', 1, 1, 'test')
    removeProduct(1)