import main
while True:
    reply = input("What would you like? (espresso/latte/cappuccino):\n")
    if reply == "espresso":
        if main.MENU["espresso"]["ingredients"]["water"] <= main.resources["water"]:
            if main.MENU["espresso"]["ingredients"]["coffee"] <= main.resources["coffee"]:
                print(f"Enter the money: {main.MENU['espresso']['cost']}")
                quarters = int(input("Enter the no. of quarters:\n"))
                dimes = int(input("Enter the no. of dimes:\n"))
                nickel = int(input("Enter the no. of nickel:\n"))
                pennies = int(input("Enter the no. of pennies:\n"))
                total_money = float(quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01)
                if main.MENU["espresso"]["cost"] <= total_money:
                    print("Thanks for the purchase here is your espresso")
                    main.resources["water"] -= main.MENU["espresso"]["ingredients"]["water"]
                    main.resources["coffee"] -= main.MENU["espresso"]["ingredients"]["coffee"]
                    change = float(total_money-main.MENU["espresso"]["cost"])
                    if change != 0:
                        print(f"Here is your remaining change : {round(change, 2)}")
                else:
                    print("Not sufficient money")
                    print(f"Here is your refund: {total_money}")
            else:
                print("Not enough coffee")
        else:
            print("Not enough water")
    elif reply == "latte":
        if main.MENU["latte"]["ingredients"]["water"] <= main.resources["water"]:
            if main.MENU["latte"]["ingredients"]["coffee"] <= main.resources["coffee"]:
                if main.MENU["latte"]["ingredients"]["milk"] <= main.resources["milk"]:
                    print(f"Enter the money : {main.MENU['latte']['cost']}")
                    quarters = int(input("Enter the no. of quarters:\n"))
                    dimes = int(input("Enter the no. of dimes:\n"))
                    nickel = int(input("Enter the no. of nickel:\n"))
                    pennies = int(input("Enter the no. of pennies:\n"))
                    total_money = float(quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01)
                    if main.MENU["latte"]["cost"] <= total_money:
                        print("Thanks for the purchase here is your latte")
                        main.resources["water"] -= main.MENU["latte"]["ingredients"]["water"]
                        main.resources["coffee"] -= main.MENU["latte"]["ingredients"]["coffee"]
                        main.resources["milk"] -= main.MENU["latte"]["ingredients"]["milk"]
                        change = float(total_money-main.MENU["latte"]["cost"])
                        if change != 0:
                            print(f"Here is your remaining change : {round(change, 2)}")
                    else:
                        print("Not sufficient money")
                        print(f"Here is your refund: {total_money}")
                else:
                    print("Not enough milk")
            else:
                print("Not enough coffee")
        else:
            print("Not enough water")
    elif reply == "cappuccino":
        if main.MENU["cappuccino"]["ingredients"]["water"] <= main.resources["water"]:
            if main.MENU["cappuccino"]["ingredients"]["coffee"] <= main.resources["coffee"]:
                if main.MENU["cappuccino"]["ingredients"]["milk"] <= main.resources["milk"]:
                    print(f"Enter the money : {main.MENU['cappuccino']['cost']}")
                    quarters = int(input("Enter the no. of quarters:\n"))
                    dimes = int(input("Enter the no. of dimes:\n"))
                    nickel = int(input("Enter the no. of nickel:\n"))
                    pennies = int(input("Enter the no. of pennies:\n"))
                    total_money = float(quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01)
                    if main.MENU["cappuccino"]["cost"] <= total_money:
                        print("Thanks for the purchase here is your cappuccino")
                        main.resources["water"] -= main.MENU["cappuccino"]["ingredients"]["water"]
                        main.resources["coffee"] -= main.MENU["cappuccino"]["ingredients"]["coffee"]
                        main.resources["milk"] -= main.MENU["cappuccino"]["ingredients"]["milk"]
                        change = float(total_money-main.MENU["cappuccino"]["cost"])
                        if change != 0:
                            print(f"Here is your remaining change : {round(change, 2)}")
                    else:
                        print("Not sufficient money")
                        print(f"Here is your refund: {total_money}")
                else:
                    print("Not enough milk")
            else:
                print("Not enough coffee")
        else:
            print("Not enough water")
    elif reply == "off":
        break
    elif reply == "report":
        for i in main.resources:
            print(f"{i}: {main.resources[i]}")
    else:
        print("Not a valid response")
