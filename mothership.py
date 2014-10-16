from cockhammer import *
from dator import *

# g = lamdba: cockhammer()

playernames = ["Cockhammer", "Dator"]
players = {"Cockhammer": cockhammer,
           "Dator": dator}


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


for i in range(len(playernames) - 1):
    player1 = playernames[i]
    for j in range(i + 1, len(playernames)):
        wins = 0
        losses = 0
        draws = 0
        stats = {"Wins": 0,
                 "Losses": 0,
                 "Draws": 0}
        player2 = playernames[j]
        for k in range(1000000):
            result = who_won(players[player1](), players[player2]())
            if result == "Win":
                stats["Wins"] += 1
            elif result == "Loss":
                stats["Losses"] += 1
            else:
                stats["Draws"] += 1
        print(stats)

# res1 = cockhammer()
# res2 = dator()
# print("Cockhammer: " + res1)
# print("Dator: " + res2)
# print(who_won(res1, res2))