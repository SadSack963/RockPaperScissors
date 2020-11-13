# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def rps_game():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    import random

    long = ["Rock", "Paper", "Scissors"]
    short = ["r", "p", "s"]
    art = [rock, paper, scissors]

    # Winning conditions
    # You Win (1)
    # You Lose (0)
    # Tie (-)
    choice_rock = ["-", "0", "1"]
    choice_paper = ["1", "-", "0"]
    choice_scissors = ["0", "1", "-"]
    win_array = [choice_rock, choice_paper, choice_scissors]

    print("Rock, Paper, Scissors Game\n")

    # User choice
    choice = input("Choose - R / P / S : ").lower()
    user_choice = 0
    for x in short:
        if choice != x:
            user_choice += 1
        else:
            break

    if user_choice <= 2:
        print(f"You chose {long[user_choice]}\n{art[user_choice]}")
    else:
        print("Invalid choice - You Lose")

    # Computer choice
    ai_choice = random.randint(0, 2)
    print(f"Computer chose {long[ai_choice]}\n{art[ai_choice]}")

    # Output
    if user_choice <= 2:
        if win_array[user_choice][ai_choice] == "1":
            print("You Win")
        elif win_array[user_choice][ai_choice] == "0":
            print("You Lose")
        else:
            print("Tie")
    else:
        print("Invalid choice - You Lose")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rps_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
