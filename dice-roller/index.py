import random

dice_draw = {
        1: (
            "---------",
            "|       |",
            "|   o   |",
            "|       |",
            "---------",
        ),
        2: (
            "---------",
            "|  o    |",
            "|       |",
            "|    o  |",
            "---------",
        ),
        3: (
            "---------",
            "| o     |",
            "|   o   |",
            "|     o |",
            "---------",
        ),
        4: (
            "---------",
            "| o   o |",
            "|       |",
            "| o   o |",
            "---------",
        ),
        5: (
            "---------",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "---------",
        ),
        6: (
            "---------",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "---------",
        ),

    }

def roll_dice():
    shall_roll = input("Shall we roll the dice? ")

    while shall_roll.lower() == "yes" or shall_roll.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled {} & {}".format(dice1, dice2))

        print("\n".join(dice_draw[dice1]))
        print("\n".join(dice_draw[dice2]))

        shall_roll = input("Roll again? ")
    print("Closing program... ")

roll_dice()