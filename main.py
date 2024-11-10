from data import resources, quarter, dime, nickle, penny, espresso, flat_white, cappuccino


def check_resources(user_order):
    """Check if there are resources to make the coffee order"""
    global off
    if resources["water"] <= user_order["water"]:
        print(f"Sorry there is not enough water left! Refill")
        off = True
        return False
    else:
        resources["water"] -= user_order["water"]

    if "milk" in user_order:
        if resources["milk"] <= user_order["milk"]:
            print(f"Sorry there is not enough milk left! Refill")
            off = True
            return False
        else:
            resources["milk"] -= user_order["milk"]

    if resources["coffee"] <= user_order["coffee"]:
        print(f"Sorry there is not enough coffe left! Refill")
        off = True
        return False
    else:
        resources["coffee"] -= user_order["coffee"]

    return True


def compare_price(inserted, user_order):
    """Check and compare the price of item with the inserted value"""
    if inserted < user_order["price"]:
        print(f"Sorry, not enough coins")
    elif inserted == user_order["price"]:
        print(f"Here is your {user_order["name"]} Enjoy!")
        resources["money"] += user_order["price"]
    elif inserted > user_order["price"]:
        change = round(inserted - user_order["price"], 2)
        resources["money"] += user_order["price"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_order["name"]} ☕ Enjoy!")


def ask_for_money():
    print("Please insert coins.")
    quarters = int(input(f"How many quarters? "))
    dimes = int(input(f"How many dimes? "))
    nickles = int(input(f"How many nickles? "))
    pennies = int(input(f"How many pennies? "))

    total_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_inserted


off = False

while not off:
    order = input(f"What would you like? (espresso/flat white/cappuccino)\n")

    if order == 'off':
        off = True
        # break
    elif order == 'report':
        print(
            f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {resources["money"]}")
        order = input(f"What would you like? (espresso/flat white/cappuccino)\n")
    elif order == 'espresso':
        if check_resources(espresso):
            money = ask_for_money()
            compare_price(money, espresso)
            print(resources)
    elif order == 'cappuccino':
        if check_resources(cappuccino):
            money = ask_for_money()
            compare_price(money, cappuccino)
            print(resources)
    elif order == 'flat white':
        if check_resources(flat_white):
            money = ask_for_money()
            compare_price(money, flat_white)
            print(resources)
    elif order == 'refill':
        resources["water"] = 200
        resources["milk"] = 500
        resources["coffee"] = 100
    else:
        print("We don't have that!")
