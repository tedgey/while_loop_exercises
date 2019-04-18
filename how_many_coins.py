# How many coins?


coins = 0

should_run = True

while should_run:
    user_input = input("You have " + str(coins) + " coins. Do you want another? ")
    if user_input == "yes":
        coins += 1
    elif user_input == "no":
        should_run = False

        print("Bye")
    else:
        print("I asked you a question.")