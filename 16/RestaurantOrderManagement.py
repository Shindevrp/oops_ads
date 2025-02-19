class MenuItem:
    def __init__(self,itemID,name,price) -> None:
        self.itemID = itemID
        self.name = name
        self.price = price
    def getItemDetails(self):
        return f" itemID {self.itemID} name {self.name} price {self.price}"

class Order:
    def __init__(self,orderID,items,tableNumber) -> None:
        self.orderID = orderID
        self.items = items #[]
        self.tableNumber = tableNumber
    
    def addItem(self,MenuItem):
        self.items.append(MenuItem)
    def calculateTotal(self):
        TotalPrice=0
        for i in self.items:
            TotalPrice+=float(i.price)
        return TotalPrice
    def removeItem(self,itemID  ):
        for i in self.items:
            if i.itemID==itemID:
                self.items.remove(i)
                return True
        return False
class OrderManager:
    def __init__(self,orders) -> None:
        self.orders=orders #[]
        

    def createOrder(self,Order):
        self.orders.append(Order)
    

    def cancelOrder(self,orderID):
        for i in self.orders:
            if i.orderID==orderID:
                self.orders.remove(i)
                return True
        return False

    def getOrder(self,orderID):
        for i in self.orders:
            if i.orderID==orderID:
                return i
                
        return None
        

