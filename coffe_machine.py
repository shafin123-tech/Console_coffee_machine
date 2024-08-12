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
    "water": 400,
    "milk": 300,
    "coffee": 100
    #"money": profit
}

# print reprt
def Check_resources_sufficient(drink):
    print("drink func",drink)
    for item in drink["ingredients"]:
        print(item)
        if drink["ingredients"][item] >= resources[item]:
            print(drink["ingredients"][item])
            print("resource item", resources[item])
            print(f"Sorry there is not enough, {item}")
            return  False
    return  True


def process_coins():
    # Prompt the user to insert coins
    print("Please insert coins.")
    try:
        # Collect the number of each type of coin
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except KeyError as e:
        print(f" please enter a valid number : {e}")

    # Calculate the total monetary value
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    print(total)

    # Return the total amount
    return total

def Check_transaction_successful(drink):
    cost = drink["cost"]
    print("cost", cost)
    payed =  round(process_coins())
    print("payed", payed)
    change =  round(payed -cost,2)

    if payed >= cost:
        print("payed succ")
        if change >0:
            print(f"you get back money change {change}")
        # return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        # return False


def item_calclution(drink):
    for item in drink["ingredients"]:
        resources[item] -=  drink["ingredients"][item]
        # print(resources[item])
        print(f" key: {item}: value: {resources[item]}")



print("resource item", resources["water"])
print("dict_menu", MENU["latte"])
print("latte ingredient", MENU["latte"]["ingredients"])
for item in MENU["latte"]["ingredients"]:
    print("latte ingrdient->", item)

state_machine = True

while state_machine == True:
    try:
        choice = input("what would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            state_machine = False
        elif choice == "report":
            print(f"resources {resources}" )
        else:
            ordered_drink = MENU[choice]
            print("order_drink", choice)
            print("ordered drink_ingredients", ordered_drink)
            print(("ordered drink_ingredients_item", ordered_drink["ingredients"]))
            if  Check_resources_sufficient(ordered_drink):
                # payment = process_coins()
                Check_transaction_successful(ordered_drink)
                item_calclution(ordered_drink)
    except KeyError as e:
        print(f"Error: {e}. Please select a valid drink.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")