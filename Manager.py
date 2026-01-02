#MANAGER'S ACCOUNT
print(f"Welcome, Manager")
###LOGIN INFO###



def day():
    activity=input("Add items(a) or change price(b)?")
    #lists
    Accepted=["add items", "a", "b", "change price"]
    Fruits=dict(mango=30, cherry=15, apple=20, banana=40)
    if activity.lower() in Accepted[0:2]:
        def add_item():
            new_fruit=input("what new item would you like to add? ")
            if new_fruit not in Fruits.keys():
                def prices():
                    while True:
                        try:
                            new_price=int(input("How much? "))
                            print("Added Successfully")
                            print("..........")
                            break
                        except ValueError:
                            print("Please enter a number! ")
                    Fruits[new_fruit]=new_price
                    for key, values in Fruits.items():
                        print(f"{key} are presently being sold at ${values}")
                prices()

                        
            else:
               print("Still available! ")
               add_item()
                       
 
            done=input("Add more(yes/no)? ")
            if done.lower()== "yes":
                add_item()
            elif done.lower() == "no":
                print("Okay")
            else:
                print("Invalid Response!")


        add_item()
    elif activity.lower() in Accepted[2:4]:
        def change():
            fruit_to_change=input("Which fruit price would you like to change? ")
            if fruit_to_change.lower() in Fruits.keys():
                print(f"{fruit_to_change} is presently being sold at ${Fruits[fruit_to_change]}")
                while True:
                    try:
                        price=int(input("How much would you like to sell them? "))
                        print("Price Updated! ")
                        break
                    except ValueError:
                        print("Please enter a number! ")

            Fruits[fruit_to_change]=price
            for key, values in Fruits.items():
                print(f"{key} is being sold at ${values}")
        change()
    else:
        print("Invalid Entry!")
        day()


    
    
manager=True
while manager:
    day()
    Choice=input("Are you done for the day(Y/N): ")
    if Choice.upper() == "Y":
        manager=False
        print("Goodbye")
    elif Choice.upper() == "N":
        manager=True
    else:
        print("invalid response")  