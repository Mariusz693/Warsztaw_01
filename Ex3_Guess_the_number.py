list_answer = ("To big", "To small", "You win")


def your_answer():
    while True:
        answer = input("Answer: ")
        if answer in list_answer:
            return answer
        else:
            print(f"Not possible answer, use {list_answer}")


def guess_number():
    print("Think the number from 0 to 1000")
    print(f"Your possible answer {list_answer}")
    min_number = 0
    max_number = 1000
    step = 1
    input("Press enter to continue ")
    while True:
        guess = int((max_number-min_number) / 2) + min_number
        print(f"Step {step}: Guessing, your number is: {guess}")
        answer = your_answer()
        if answer == "You win":
            print(f"Win, the number is {guess} !!!!")
            break
        elif answer == "To big":
            max_number = guess
            step += 1
        elif answer == "To small":
            min_number = guess
            step += 1
        else:
            print("Do not cheat")


if __name__ == '__main__':
    guess_number()
