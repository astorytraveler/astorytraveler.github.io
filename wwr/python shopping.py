
option_number = ""
items_cart = []
prices_cart = []

total = 0

i = None

while option_number != 6:
    print ("-----------")
    print ("\nPlease select one of the following:")
    print ("1. Add item\n2. Remove an item\n3. View cart\n4. Compute the Total\n5. Highest priced item\n6. Quit")
    option_number = int(input("Please select an option number: "))
    
    if option_number == 1:
        item = input(f"\nWhat item would you like to add? ")
        items_cart.append(item)
        price = float(input (f"\nWhat is the price of {item}"))
        prices_cart.append(price)
        print(f"{item} at ${price:.2f} has been added to the cart.")

    if option_number == 2:
        items_to_remove = int(input(f"\nWhat item number would you like to remove? "))
        items_cart.pop(items_to_remove-1)
        prices_cart.pop(items_to_remove-1)
        print(f"\nItem number {items_to_remove} has been removed.\n")

    if option_number == 3:
        print ("\nThe content of your shopping cart are: ")
        for i in range(len(items_cart)):
            print(f"{i+1}. {items_cart[i]} - {prices_cart[i]:.2f}")

    if option_number == 4:
        total = sum (prices_cart)
        print (f"Your cart total is ${total}.")

    if option_number == 5:
        largest_number = prices_cart[0]
        for number in prices_cart:
            if number > largest_number:
                largest_number = number
        print(f"The highest price in your cart is ${largest_number}")

print ("\nThank you. Goodbye.")
