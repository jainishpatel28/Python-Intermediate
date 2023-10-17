# Starting to build Coffee-Machine program

# imports
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_ingredients):
    """Returns True when drinks can be made, Returns False when ingredients are insufficient"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def count_coins():
    """Asks about inserting coins, and counting total money inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_checking(money_received, drink_price):
    """comparing the money received and drink price, Returns change or refund."""
    if money_received >= drink_price:
        change = round(money_received - drink_price, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the resources used to make coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")


machine_off = True
while machine_off:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "off":
        machine_off = False
    elif prompt == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[prompt]
        if check_resources(drink['ingredients']):
            payment = count_coins()
            if transaction_checking(payment, drink["cost"]):
                make_coffee(prompt, drink["ingredients"])




