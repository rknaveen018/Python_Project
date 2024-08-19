base = {"B1": ["Small Pizza", 1], "B2": ["Medium Pizza", 1.5], "B3": ["Large Pizza", 2]}
pizza = {"P1": ["Margherita", 3], "P2": ["Veg Extravaganza", 3.5], "P3": ["Veggie Paradise", 3],
         "P4": ["Pepper Barbecue Chicken", 3.5], "P5": ["Farmhouse", 3]}
topping = {"T1": ["Olives", 0.5], "T2": ["Extra Cheese", 0.5], "T3": ["Mushrooms", 0.5], "T4": ["Green Peppers", 0.5]}


def order():
    name = input("Enter the name : ")
    phone_number = input("Enter your phone number : ")
    while True:
        if name.isalpha():
            break
        else:
            print("Entered name is invalid")
            name = input("Enter the name : ")

    while True:
        if phone_number.isnumeric() and phone_number[0] in "9876" and len(phone_number) == 10:
            break
        else:
            print("Entered number is invalid")
            phone_number = input("Enter your phone number : ")

    for i, j in base.items():
        print("ID ", ": ", i, "|", "Size", ": ", j[0], "|", "Price ", ": ", j[1])

    choose_size = input("Choose ID from above : ")
    if choose_size.upper() in base.keys():
        pass
    else:
        print("Selected invalid ID")
        choose_size = input("Choose ID from below : ")

    for i, j in pizza.items():
        print("ID ", ": ", i, "|", "Size ", ": ", j[0], "|", "Price ", ": ", j[1])

    choose_pizza = input("Choose ID from above : ")
    if choose_pizza.capitalize() in pizza.keys():
        pass
    else:
        print("Selected invalid ID")
        choose_pizza = input("Choose ID from below : ")

    for i, j in topping.items():
        print("ID ", ": ", i, ": ", "Size ", ": ", j[0], ": ", "Price ", ": ", j[1])

    topping_list = []
    n = int(input("Enter the number of topping want : "))
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    while True:
        if n <= 2 or n in num_list:
            break
        else:
            print("Please enter a number of topping less than 3")
            n = input("Enter the number of topping want : ")

    for i in range(n):
        choose_toppings = input("Choose ID from above : ")
        if choose_toppings.capitalize() in topping.keys():
            topping_list.append(choose_toppings.upper())
        else:
            for m, j in topping.items():
                print("ID ", ": ", m, "Size ", j[0], ": ", "Price ", j[1])
            print("Selected invalid ID")
            choose_toppings = input("Choose ID from above : ")

    return choose_size.upper(), choose_pizza.upper(), topping_list


def bill_details(x):
    print("Food", ":", base.get(x[0])[0], "Price", ":", base.get(x[0])[1])
    print("Food", ":", pizza.get(x[1])[0], "Price", ":", pizza.get(x[1])[1])
    topping_price = 0
    for i in bill[-1]:
        j = 0
        print("Food", topping.get([i][j])[0], "Price", topping.get([i][j])[1])
        topping_price += topping.get([i][j])[1]
        j += 1
    print("Total", base.get(x[0])[1] + pizza.get(x[1])[1] + topping_price)


while True:
    bill = order()
    num = input("Do you want to place another order(Yes/No) : ")
    while num.capitalize() == "Yes":
        order()
        num = input("Do you want to place another order(Yes/No) : ")
    else:
        print("Thanks your order below are the details for the same enjoy your food")
        bill_details(bill)
        break

