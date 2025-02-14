name = input("Enter your name: ")
print("Hello " + name + " welcome to my game")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes":
    print("We are going to play!")

    direction = input("Do you want to go left or right? (lefty/right) ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, game over, try again.")

    elif direction == "right":
        choice = input("Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) ")

        if choice == "swim":
            print("you got eaten by an alligator, you die, the end!")
                  
        else: print("You found the gold and won!")

    else: print("sorry not a valid reply, you die!")