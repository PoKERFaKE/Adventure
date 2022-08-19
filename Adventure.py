
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("you're on a dark forest, there are two ways right and left which way do you choose? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an aligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge, it looks creepy, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and helped him out and for reward he gave alot of gold . You WIN!")
        elif answer == "no":
            print("You ignored the stranger and didn't help him and then u were eaten  by an anaconda , (you should help people freak) .")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)