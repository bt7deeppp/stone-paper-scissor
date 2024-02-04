import random
Player1 = random.randrange(1 , 4)
Player1Copy = Player_1

print("1-Stone ┃ 2-Paper ┃ 3-Scissor")
Player2 = int(input("Enter your move: "))

if Player1Copy == 1:
    Player1Copy = "Stone"
elif Player1Copy == 2:
    Player1Copy = "Paper"
else:
    Player1Copy = "Scissor"


if Player1 == 1 and Player2 == 2 or Player1 == 2 and Player2 == 3 or Player1 == 3 and Player2 == 1:
    print("You Win! - Computer Chose",Player1Copy)

elif Player1 == 1 and Player2 == 3 or Player1 == 2 and Player2 == 1 or Player1 == 3 and Player2 == 2:
    print("You Lose - Computer Chose",Player1Copy)

else:
    print("The game is a Draw")




