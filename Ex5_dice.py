from random import randint

list_dice = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def throws_dice(dice_text):
    user_dice = ""
    for dice in list_dice:
        if dice in dice_text:
            user_dice = dice
    if user_dice == "":
        return "Wrong Value"
    dice_size = int(user_dice[1:])
    position_d = 0
    len_dice_text = len(dice_text)
    for i in range(len_dice_text):
        if dice_text[i] == "D":
            position_d = i
    number_of_throws = dice_text[:position_d]
    if number_of_throws == "":
        number_of_throws = 1
    else:
        try:
            number_of_throws = int(number_of_throws)
        except ValueError:
            return "Wrong Value"
    position_extra = position_d + len(user_dice)
    extra_value = dice_text[position_extra:]
    if extra_value == "":
        extra_value = 0
    else:
        try:
            extra_value = int(extra_value)
        except ValueError:
            return "Wrong Value"
    sum_throws = 0
    for i in range(number_of_throws):
        sum_throws += randint(1, dice_size)

    return sum_throws + extra_value


def throws_dice_2(dice_text):
    look_dice = ""
    for dice in list_dice:
        if dice in dice_text:
            look_dice = dice
    if look_dice == "":
        return "Wrong Value"
    try:
        number, extra = dice_text.split(look_dice)
    except ValueError:
        return "Wrong Value"
    size_dice = int(look_dice[1:])
    try:
        number = int(number) if number else 1
    except ValueError:
        return "Wrong Value 2"
    try:
        extra = int(extra) if extra else 0
    except ValueError:
        return "Wrong Value 3"
    sum_throws = sum([randint(1, size_dice) for _ in range(number)])

    return sum_throws + extra


if __name__ == '__main__':
    print(throws_dice("2D10-15"))
    print(throws_dice("D6"))
    print(throws_dice("2D3+k"))
    print(throws_dice("D12-1"))
    print(throws_dice("4-3D6"))
    print()
    print(throws_dice_2("2D10-15"))
    print(throws_dice_2("D6"))
    print(throws_dice_2("2D3+k"))
    print(throws_dice_2("D12-1"))
    print(throws_dice_2("4-3D6"))
