import random
while True:
    a = random.randrange(1,10)

    print("Guess The Game")
    for i in range(1,4):
        player = int(input("Guess The Number: "))
        if player == a:
            print("Welldon!\nYou Did It")
            break
        else:
            print("Try Again")
    print("Game Over")
    print("Exit From The Game press 1 else 2")
    exit_ = int(input())
    if exit_ == 2:
        pass
    else:
        print("Thank's For Playing")
        break

    
