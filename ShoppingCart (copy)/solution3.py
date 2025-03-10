class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity  

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class Cart:
    def __init__(self):
        self.ct = {}  

    def Add_Item(self, name, price, quantity):
        if name in self.ct:
            self.ct[name]['quantity'] += quantity 
            print(f"Quantity updated for item: {name}")
        else:
            self.ct[name] = {'price': price, 'quantity': quantity}
            print(self.ct) 
            print(f"Item added to cart: {name}")

    def Remove_Item(self, name):
        if name not in self.ct:
            print(f"Item not found in the cart: {name}")
        else:
            del self.ct[name]  
            print(f"Item removed from cart: {name}")

    def Display_Items(self):
        if len(self.ct) == 0:
            print("Cart is empty.")
        else:
            print("Items in Cart:")
            total = 0
            for name, v in self.ct.items():
                item_total = v['price'] * v['quantity']
                total += item_total
                print(f"{name} - ${v['price']:.2f} * {v['quantity']} = ${item_total:.2f}")
            print(f"Total Amount: ${total:.2f}")

    def Calculate_Total_Amount(self):
        total = 0
        for item in self.ct:
            total += self.ct[item]['price'] * self.ct[item]['quantity']
        return total

    def Apply_Discount(self):
        total = self.Calculate_Total_Amount()
        discount = total * 0.10
        after_discount = total - discount
        print(f"Total after 10% discount: ${after_discount:.2f}")

    def runCart(self):
        while True:
            try:
                i = input().split(" ")
                if i[0] == "Add":
                    name = i[2].strip(",")
                    price = float(i[3].strip(","))
                    quantity = int(i[4].strip(","))
                    self.Add_Item(name, price, quantity)
                elif i[0] == "Remove":
                    self.Remove_Item(i[2].strip(","))
                elif i[0] == "DisplayCart":
                    self.Display_Items()
                elif i[0] == "ApplyDiscount":
                    self.Apply_Discount()
                else:
                    break
            except:
    
                break

if __name__ == "__main__":
    cart = Cart()
    cart.runCart()
