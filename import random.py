import random
player_score=0
ai_score=0
x=True
print("Scoreboard:",player_score,":",ai_score)
while x== True:
    player=str(input("Choose rock,paper,scissor?:"))
    ai=random.choice(["rock","paper","scissor"])
    print(player, "v.s", ai)
    if player==ai:
        print("It's a draw!")
    elif player=="rock":
        if ai=="scissor":
            print("Congrats you won!")
            player_score+=1
            ai_score+=0
        else:
            print("You lose!")
            player_score+=0
            ai_score+=1
    elif player=="scissor":
        if ai=="paper":
            print("Congrats you won!")
            player_score+=1
            ai_score+=0
        else:
            print("You lose!")
            player_score+=0
            ai_score+=1
    elif player=="paper":
        if ai=="rock":
            print("Congrats you won!")
            player_score+=1
            ai_score+=0
        else:
            print("You lose!")
            player_score+=0
            ai_score+=1 
    print("Scoreboard:",player_score,":",ai_score)
    again=str(input("Would you like to play again, yes or no?:"))
    if again == "yes":
        x=True
    else:
        x=False
