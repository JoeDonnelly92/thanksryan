from random import randint

def main():
    level = get_level()
    for i in range(0, 3):
        play_game(level)


def get_level():
    #Uses While loop to prompt user until a positive int between 1 and 3 is provided.
    while True:
        level = input("Level: ")
        if level.isdigit() == True:
            level = int(level)
            if 1 <= level <= 3:
                return level


def play_game(level):
    #Generate 2 random integers, x and y with a number of digits equal to 'level' variable.
    a = randint(0, 10**level-1)
    b = randint(0, 10**level-1)
    #Prompt user for input and check if it is equal to x+y
    answer = int(input(f"{a} + {b} = "))
    if answer == a + b:
        #If input is equal, congratulate user and break loop
        print("Correct!")
    else:
        #If it is not equal, print EEE and give user 2 further attempts.
        for i in range(0, 2):
            print("EEE")
            answer = int(input(f"{a} + {b} = "))
            if answer == a + b:
                print("Correct!")
                break
        #If no correct answer given within 3 attempts, print answer.
        print(f"{a} + {b} = {a+b}")

if __name__ == "__main__":
    main()
