from models import *

db = SqliteDatabase('betsyWebshop.db')


def searchProducts(searchString):
    name_results = Product.select().where(Product.name.contains(searchString))
    description_results = Product.select().where(Product.description.contains(searchString))
    products = name_results.union(description_results)
    return products


def searchProductsByTag(tags):
    return Product.select().where(Product.tags.contains(ProductTag.select().where(ProductTag.tag == tags)))


def searchProductsByOwner(userid):
    return Product.select().where(Product.owner.contains(userid))


def addProduct(name, price, description, stock, owner, tags):
    tag = ProductTag.create(tag=tags)
    Product.create(name=name, price=price, description=description, stock=stock, owner=owner, tags=tag)


def addTagToProduct(productid, tag):
    ProductTag.create(tag=tag, product=productid)


def removeProduct(productid):
    ProductTag.delete().where(ProductTag.product == productid).execute()
    Product.delete().where(Product.productId == productid).execute()


def updateStock(productid, newStock):
    Product.update(stock=newStock).where(Product.productId == productid)


def addPurchase(userid, productid, quantity):
    Purchase.create(buyer=userid, product=productid, quantity=quantity)
    updateStock(productid, Product.select().where(Product.productId == productid).stock - quantity)


def create_tables():
    with db:
        db.drop_tables([User, Product, Purchase])
        db.create_tables([User, Product, Purchase])


def populate_tables():
    i = 0
    while i < 10:
        tags = 'tag ' + str(i)
        User.create(username='test', adress='test', billingInfo='test')
        ProductTag.create(tag=tags)
        Product.create(name='test', price=1.0, description='test', stock=1, owner=1,
                       tags=(ProductTag.select().where(ProductTag.tag == tags)))
        i += 1
    print('Tables populated!')


if __name__ == '__main__':
    # create_tables()
    # populate_tables()
    print(searchProducts('test'))
    # searchProductsByTag('test')
    # searchProductsByOwner(1)
    # addProduct('test', 1.0, 'test', 1, 1, 'test')
    # removeProduct(1)
