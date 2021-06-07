import random

print("\nHi, welcome to dungeon. You need to pay $5 to play")
print("If you face a monster, you will lose the game and $5 you paid.")
print("But if you find a money ($5, $10, $15, $20), you will earn money that you find")

global status, money
status = [0, 0, 0]  # win / lose / money that earned
money = [0, 0, 0, 0, 0] #0, 5, 10, 15, 20


def direction():
    direction = input("Where do you want to go? Left or Right? (L or R)")
    print(direction)
    return direction


def earn(x):

    if x == 5:
        money[1] += 1
    elif x == 10:
        money[2] += 1
    elif x == 15:
        money[3] += 1
    elif x == 20:
        money[4] += 1

    status[0] += 1
    status[2] += x
    print("\nYou escaped with earning $", x, "    Profit:", x-5)

    return status, money


def monster():
    print("You died by a monster. Game End")
    status[1] += 1
    money[0] += 1
    return status, money


def randomDirection():
    randomDirection = random.choice(["L", "R"])
    print(randomDirection)
    return randomDirection


def auto():

    if randomDirection() == "L":
        if randomDirection() == "L":
            earn(5)
        else:
            if randomDirection() == "R":
                monster()

            else:
                if randomDirection() == "L":
                    earn(15)
                else:
                    earn(10)
    else:
        if randomDirection() == "L":
            monster()
        else:
            if randomDirection() == "R":
                earn(5)
            else:
                if randomDirection() == "L":
                    earn(20)
                else:
                    monster()

    return status


def manual():
    if direction() == "L":
        if direction() == "L":
            earn(5)
        else:
            if direction() == "R":
                monster()
            else:
                if direction() == "L":
                    earn(15)
                else:
                    earn(10)
    else:
        if direction() == "L":
            monster()
        else:
            if direction() == "R":
                earn(5)
            else:
                if direction() == "L":
                    earn(20)
                else:
                    monster()


while True:
    status = [0, 0, 0]
    print("\nOptions: Manual or Automatic or End the game (M or A or E)")
    method = input("Choose operation mode among the above options: ")
    if method == "M":
        print()
        manual()
    elif method == "A":
        count = int(input("\nHow many times do you want to repeat the game?: "))

        if count is not int:
            print("please input integer")
        for i in range(1, count + 1):
            auto()
        print("\nWin: ", status[0], "| Lose: ", status[1], "| Income: ", status[2], "| Cost: ", count * 5, "| Profit: ", status[2] - (count * 5))
        print("Monster: ", money[0], "$5: ", money[1], "$10: ", money[2], "$15: ", money[3], "$20: ", money[4])

    elif method == "E":
        break
    else:
        print("\n Insert M or A or E again")
