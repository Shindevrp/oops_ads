class Product:
    def __init__(self,productId,name,price,quantyItStock) -> None:
        self.productId = productId
        self.name =  name
        self.price = price
        self.quantyItStock = quantyItStock

    def updataStock(self,quantity):
    
        self.quantyItStock+=quantity


    def getProductInfo(self):
        return f"productId {self.productId} name {self.name} price {self.price} quantyItStock {self.quantyItStock}"

class Inventory:
    def __init__(self,product):
        self.products =product

    def addProduct(self,product):
        self.products.append(product)

    
    def updateProductStock(self,productId,quantity):
        for Product in self.products:
            # print(productId)
            if Product.productId==productId:
                
                Product.quantyItStock+=quantity
                return True
        return False
                



    def listProducts(self):
        return self.products