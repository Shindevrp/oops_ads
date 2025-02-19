from RestaurantOrderManagement import MenuItem,Order,OrderManager
def main():
    # Create menu items
    item1 = MenuItem(1, "Burger", 8.5)
    item2 = MenuItem(2, "Fries", 3.0)
    item3 = MenuItem(3, "Soda", 2.0)
    # Create an order and add items
    order = Order(101, [], 5)
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    total = order.calculateTotal()
    print("Calculated total:", total)
    # Remove an item and recalc total

    removed = order.removeItem(2)
    print("Item 2 removed:", removed)
    print("New total after removal:", order.calculateTotal())
    # Test OrderManager functionality
    om = OrderManager([])
    om.createOrder(order)
    retrieved_order = om.getOrder(101)
    print("Retrieved order for table", retrieved_order.tableNumber)
    cancelled = om.cancelOrder(101)
    print("Order cancellation status:", cancelled)
if __name__ == '__main__':
    main()