class item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quatity=quantity

    
    # def Update_Quantity(self):
    #     if 
        
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
class cart:
    def __init__(self):

        self.item=[]
        self.ct={}
        
    def Add_Item(self,name,price,quantity):
        # print("working")
        if name in self.ct:
    
            self.ct[name]['quantity'] += quantity
            print(f"Item updated in cart: {name}")
        else:
    
            self.ct[name] = {'price': price, 'quantity': quantity}
            print(f"Item added to cart: {name}")
   
        
    def Remove_Item(self,name):
        if name not in self.ct:
            print(f"Item not found in the cart: {item}")
        else:
            del self.ct[name]
            print(f"Item removed from cart: {name}")
        # for i in self.ct:
        #     if i.name==item.name:
        #         self.ct.remove(i)
        #         self.ct.remove(i+1)
        #         self.ct.remove(i+2)

            
    def Display_Items(self):
        
        if len(self.ct)==0:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for name, details in self.ct.items():
                print(f"{name} - Price: {details['price']}, Quantity: {details['quantity']}")
    def Calculate_Total_Amount(self):
        total=0
        for i in self.ct:
            total+= i['price'] * i['quantity']
        return total

    def Apply_Discount(self):

        discount=self.Calculate_Total_Amount()*0.10
        after_discount=self.Calculate_Total_Amount()-discount
        print(f"Total after 10% discount: {after_discount}")
        
    def Apply_Coupon(self):
        pass
    def Checkout(self):
        pass
    def runCart(self):


        while True:
            try:
                i = input().split(" ")
                # print(i)
                if i[0]=="Add":
                    # print((i[2].strip(",")))
                    # print("hi")
                    a = i[2].strip(",")
                    # print(a)
                    self.Add_Item(a,1,2)
                elif i[0] == "Remove":
                    self.Remove_Item(i[2].strip(","))
                    
                elif i[0]=="DisplayCart":
                    self.Display_Items()
                elif i[0]=="ApplyDiscount":
                    self.Apply_Discount()
            except:
                break

if __name__=="__main__":
    c=cart()
    c.runCart()
            
