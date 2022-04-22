name = input("Hello fellow adverturer, what is your name?: ")
print("Greetings", name, "prepare to sail out on this open sea adventure!!")

answer = input(
    "You are currently on a pirate ship, do you want to take the safe route or the shortcut?: ").lower()

if answer == "shortcut":
    answer = input(
        "A fishy looking ship member offer you a bowl of food. Do you eat it or leave it?:  ")

    if answer == "leave":
        print("you left the food and someone else ate it and died from poisoning. After a while, you ran into moby dick and was sunken and drowned. Better luck next time!!")
    elif answer == "eat":
        print("Yyou got poisoned to death by the food. LOL")
    else:
        print('Not a valid option. You lose.')

elif answer == "safe":
    answer = input(
        "After what it seems like an eternity, you finally arrive to the hidden island. Do you wander alone or follow the group? (follow/wander) ")

    if answer == "follow":
        print("you follow the group and found the treasure but they wanted it for themselves and you end up getting killed.")
    elif answer == "wander":
        answer = input(
            "you found the treasure yourself, do you take it back alone or tell the crew members?(alone/tell) ")

        if answer == "alone":
            print("you bring the treasure back to the ship secretly and sail home safely, becoming the richest person alive. CONGRATS, YOU'VE WON!!!")
        elif answer == "no":
            print("the crew members are greedy and murder you and take the treasure for themselves. Hey, at least you had a good heart and wanted to share.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)