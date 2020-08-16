from random import randint
from Ex5_dice import throws_dice, list_dice


def add_points(player_points):
    points = sum([randint(1, 6) for _ in range(2)])
    if points == 7:
        player_points //= 7
    elif points == 11:
        player_points *= 11
    else:
        player_points += points
    return player_points


def game_2001():
    player_1 = 0
    player_2 = 0
    step = 1
    print("Game 2001, You play with computer")
    print(f"Your points: {player_1}")
    print(f"Computer points: {player_2}")
    input("Press Enter to start rolls the dice")
    player_1 = sum([randint(1, 6) for _ in range(2)])
    player_2 = sum([randint(1, 6) for _ in range(2)])

    while (player_1 < 2001) and (player_2 < 2001):
        print()
        print(f"Step {step}")
        print(f"Your points: {player_1}")
        print(f"Computer points: {player_2}")
        input("Press Enter to start rolls the dice")
        player_1 = add_points(player_1)
        player_2 = add_points(player_2)
        step += 1

    print(f"Game over, Step {step}")
    print(f"Your points: {player_1}")
    print(f"Computer points: {player_2}")
    if player_1 > player_2:
        print("You win !!!")
    elif player_1 < player_2:
        print("Computer win !!!")
    else:
        print("It's draw")


def add_points_2(player_points, dice):
    points = throws_dice(dice)
    if points == 7:
        player_points //= 7
    elif points == 11:
        player_points *= 11
    else:
        player_points += points
    return player_points


def game_2001_2():
    player_1 = 0
    player_2 = 0
    step = 1
    print("Game 2001, You play with computer")
    print(f"Your points: {player_1}")
    print(f"Computer points: {player_2}")
    input("Press Enter to start rolls the dice")
    your_dice = input(f"Check your dice {list_dice}: ")
    computer_dice = list_dice[randint(1, len(list_dice))]
    print(your_dice)
    print(computer_dice)
    player_1 = throws_dice(your_dice)
    player_2 = throws_dice(computer_dice)
    while (player_1 < 2001) and (player_2 < 2001):
        print()
        print(f"Step {step}")
        print(f"Your points: {player_1}")
        print(f"Computer points: {player_2}")
        input("Press Enter to start rolls the dice")
        player_1 = add_points_2(player_1, your_dice)
        player_2 = add_points_2(player_2, computer_dice)
        step += 1

    print(f"Game over, Step {step}")
    print(f"Your points: {player_1}")
    print(f"Computer points: {player_2}")
    if player_1 > player_2:
        print("You win !!!")
    elif player_1 < player_2:
        print("Computer win !!!")
    else:
        print("It's draw")


#game_2001()
game_2001_2()
