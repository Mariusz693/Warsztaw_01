from random import randint


def check_number(number_to_check):
    try:
        number = int(number_to_check)
        return number
    except ValueError:
        print("It's not a number!")
        return None


def guess_number():
    random_number = randint(1, 100)
    while True:
        your_number = input("Guess the number: ")
        your_number = check_number(your_number)
        if your_number:
            if your_number < random_number:
                print("To small!")
            elif your_number > random_number:
                print("To big")
            else:
                print("You win")
                break


if __name__ == '__main__':
    guess_number()
