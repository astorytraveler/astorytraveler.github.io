initial_option = ""
items_cart = []
prices_cart = []

total = 0
i = None

while initial_option != 5:
    print ("-----------")
    print ("\nPlease select one of the following:")
    print ("1. Add item\n2. Remove an item\n3. View cart\n4. Compute the Total\n5. Quit")
    initial_option == int(input("Please select an option number: "))
    
    if initial_option == 1:
        item = input(f"\nWhat item would you like to add? ")
        items_cart.append(item)
        price = float(input (f"\nWhat is the price of {item}"))
        prices_cart.append(price)
        print(f"\n{item} at ${price:.2f} has been added to the cart.")

    if initial_option == 2:
        items_to_remove = int(input(f"\nWhat item number would you like to remove? "))
        items_cart.pop(items_to_remove)
        prices_cart.pop(items_to_remove)
        print(f"\nItem number {items_to_remove} has been removed.\n")

    if initial_option == 3:
        print ("\nThe content of your shopping cart are: ")
        for i in range(len(items_cart)):
            print(f"{i}. {items_cart[i]} - {prices_cart[i]:.2f}")

    if initial_option == 4:
        total = sum (prices_cart)
        print (f"Your cart total is ${total}.")

print ("\nThank you. Goodbye.\n")
