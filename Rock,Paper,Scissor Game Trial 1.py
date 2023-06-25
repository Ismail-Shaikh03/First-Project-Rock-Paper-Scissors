import random
player_score=0
ai_score=0
print("Scoreboard:",player_score,":",ai_score)
player=str(input("Choose rock,paper,scissor?:"))
ai=random.choice(["rock","paper","scissor"])
print(player, "v.s", ai)
#player_vs_ai=player>ai or player<ai or player==ai
if "rock">"scissor" or "scissor">"paper" or "paper">"rock":
    print("Congrats you won!")
    player_score=+1
    ai_score=+0
    print(player_score,":",ai_score)
elif "rock"=="rock" or "scissor"=="scissor" or "paper"=="paper":
    print("It's a draw!")
    player_score=+0
    ai_score=+0
    print(player_score,":",ai_score)
elif "rock"<"paper" or "paper"<"scissor" or "scissor"<"rock":
    print("You lose!")
    player_score=+0
    ai_score=+1
    print(player_score,":",ai_score)
else:
    print("Choose one of the 3 options!")

    
