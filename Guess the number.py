import random

secret_number = random.randint(1,100)


while True:
    askuser = (int(input("please enter a number: ")))

    if askuser < secret_number:
        print("Your number is too low, please try again")
    elif askuser > secret_number:
        print("Your number is too high, please tyr again")
    elif askuser == secret_number:
        print("the guessed the secret number")
        break;
    else:
        print("you did not get the right number")
