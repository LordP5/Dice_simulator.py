import random
def roll_dice():
    print("This is a 1 to 6 dice rolling simulator")
    while True:
        dice = random.randint(1, 6)
        roll = input("Type `r` to roll ")
        if roll.lower() == "r":
            print(dice)
        elif roll.lower() == "quit":
            print("Thanks for rolling the dice")
            break


roll_dice()

