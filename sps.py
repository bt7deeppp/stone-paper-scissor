import random
Player_1 = random.randrange(1 , 4)
Player_1_C = Player_1

print("1-Stone ┃ 2-Paper ┃ 3-Scissor")
Player_2 = int(input("Enter your move: "))

if Player_1_C == 1:
    Player_1_C = "Stone"
elif Player_1_C == 2:
    Player_1_C = "Paper"
else:
    Player_1_C = "Scissor"


if Player_1 == 1 and Player_2 == 2 or Player_1 == 2 and Player_2 == 3 or Player_1 == 3 and Player_2 == 1:
    print("You Win! - Computer Chose",Player_1_C)

elif Player_1 == 1 and Player_2 == 3 or Player_1 == 2 and Player_2 == 1 or Player_1 == 3 and Player_2 == 2:
    print("You Lose - Computer Chose",Player_1_C)

else:
    print("The game is a Draw")




