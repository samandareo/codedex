from random import randint

computer = randint(1, 4)
banner = "===================\nRock Paper Scissors\n===================\n\n"
menu = "1) ✊\n2) ✋\n3) ✌️\nPick a number: "

while True:
    player = int(input(banner + menu))

    if computer == 1 and player == 1:
        print("Computer: ✊\nPlayer: ✊\n\nIt's a tie!")
        break
    elif computer == 1 and player == 2:
        print("Computer: ✊\nPlayer: ✋\n\nPlayer wins!")
        break
    elif computer == 1 and player == 3:
        print("Computer: ✊\nPlayer: ✌️\n\nComputer wins!")
        break
    elif computer == 2 and player == 1:
        print("Computer: ✋\nPlayer: ✊\n\nComputer wins!")
        break
    elif computer == 2 and player == 2:
        print("Computer: ✋\nPlayer: ✋\n\nIt's a tie!")
        break
    elif computer == 2 and player == 3:
        print("Computer: ✋\nPlayer: ✌️\n\nPlayer wins!")
        break
    elif computer == 3 and player == 1:
        print("Computer: ✌️\nPlayer: ✊\n\nPlayer wins!")
        break
    elif computer == 3 and player == 2:
        print("Computer: ✌️\nPlayer: ✋\n\nComputer wins!")
        break
    elif computer == 3 and player == 3:
        print("Computer: ✌️\nPlayer: ✌️\n\nIt's a tie!")
        break
    else:
        print("Invalid input. Please pick a number between 1 and 3.")
        continue

