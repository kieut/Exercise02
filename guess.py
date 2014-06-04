from random import randint

def main():
    print "What's your name?"
    username = raw_input(">")
    computerNumber = randint(1, 100)
    print computerNumber
    guess = 0
    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % username
    while guess != computerNumber:
        try:
            guess = int(raw_input("Your guess?"))
        except ValueError:
            print("Not an integer!")
            continue
        if guess == computerNumber:
            print "Congratulations. You found the number."
        elif guess > computerNumber:
            print "Your number is too high."
        else:
            print "Your number is too low."
    return computerNumber

if __name__ == "__main__":
    main()





    
