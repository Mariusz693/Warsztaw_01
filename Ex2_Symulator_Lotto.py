from random import shuffle


def check_number(number_to_check):
    try:
        number = int(number_to_check)
        return number
    except ValueError:
        print("It's not a number!")
        return None


def get_numbers():
    list_numbers = []
    i = 0
    while i < 6:
        number = input(f"Give your {i+1} number: ")
        number = check_number(number)
        if number:
            if number < 1 or number > 49:
                print("Number out of range (1-49)")
            elif number in list_numbers:
                print("You have chose this number")
            else:
                list_numbers.append(number)
                i += 1
    return sorted(list_numbers)


def random_numbers():
    list_numbers = list(range(1, 50))
    shuffle(list_numbers)
    return sorted(list_numbers[:6])


def lotto():
    user_lotto = get_numbers()
    random_lotto = random_numbers()
    print("Your numbers:", user_lotto)
    print("Random numbers:", random_lotto)
    result = 0
    for i in user_lotto:
        for j in random_lotto:
            if i == j:
                result += 1
    if result < 3:
        print(f"Sorry, you lost, You hit {result} numbers")
    else:
        print(f"Congratulations, You hit {result} numbers")


if __name__ == '__main__':
    lotto()
