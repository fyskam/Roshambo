from cockhammer import *
from dator import *

playernames = ["Cockhammer", "Dator", "Lol"]
players = {"Cockhammer": cockhammer(),
           "Dator": dator()}


def who_won(res1, res2):
    if res1 == res2:
        return "Draw"
    elif res1 == "paper":
        if res2 == "rock":
            return "Win"
        else:
            return "Loss"
    elif res1 == "scissors":
        if res2 == "paper":
            return "Win"
        else:
            return "Loss"
    elif res1 == "rock":
        if res2 == "scissors":
            return "Win"
        else:
            return "Loss"
    else:
        return "WTF!"


# for i in range(len(playernames) - 1):
#     print("Turn")
#     player1 = playernames[i]
#     print(player1)
#     for j in range(i + 1, len(playernames)):
#         player2 = playernames[j]
#         print(player2)

res1 = cockhammer()
res2 = dator()
print("Cockhammer: " + res1)
print("Dator: " + res2)
print(who_won(res1, res2))