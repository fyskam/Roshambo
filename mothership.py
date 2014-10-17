from cockhammer import *
from dator import *
from dator2 import *
import pickle
import collections


playernames = ["Cockhammer", "Dator", "Dator2"]
players = {"Cockhammer": cockhammer,
           "Dator": dator,
           "Dator2": dator2}
# high_scores = {"Cockhammer": 0,
#                "Dator": 0,
#                "Dator2": 0}
# with open("highscore.pkl", "wb") as out:
#     pickle.dump(high_scores, out)


def who_won(res1, res2):
    if res1 == res2:
        return "d"
    elif res1 == "paper":
        if res2 == "rock":
            return "1"
        else:
            return "2"
    elif res1 == "scissors":
        if res2 == "paper":
            return "1"
        else:
            return "2"
    elif res1 == "rock":
        if res2 == "scissors":
            return "1"
        else:
            return "2"
    else:
        return "WTF!"


def highscore(score1, score2):
    with open("highscore.pkl", "rb") as in_:
        high_scores = pickle.load(in_)
    if score1.name not in high_scores:
        high_scores[score1.name] = 0
    high_scores[score1.name] = high_scores[score1.name] + score1.score
    if score2.name not in high_scores:
        high_scores[score2.name] = 0
    high_scores[score2.name] = high_scores[score2.name] + score2.score
    with open("highscore.pkl", "wb") as out:
        pickle.dump(high_scores, out)


for i in range(len(playernames) - 1):
    Score = collections.namedtuple("Score", ["name", "score"])
    player1 = playernames[i]
    for j in range(i + 1, len(playernames)):
        player2 = playernames[j]
        f = open('RPSdata.txt', 'r+')
        f.seek(0, 2)
        wins = 0
        losses = 0
        for k in range(100):
            res1 = players[player1]()
            res2 = players[player2]()
            result = who_won(res1, res2)
            if result == "1":
                wins += 1
            elif result == "2":
                losses += 1
            f.write(res1 + " " + res2 + " " + result + "\n")
        player1_score = Score(player1, (wins - losses))
        player2_score = Score(player2, player1_score.score * (-1))
        highscore(player1_score, player2_score)

with open("highscore.pkl", "rb") as in_:
    new_high_scores = pickle.load(in_)

print("{{TITLE:^{PAGE_WIDTH}}}".format(PAGE_WIDTH=80).format(TITLE="HIGH SCORES"))
print("-" * 80)
for name, score in new_high_scores.items():
    print("{{name:>{col_width}}} | {{score:<{col_width}}}".format(col_width=(80-3)//2).format(name=name, score=score))
