import random as ran
from os import system as sys

bk = []

with open("../booknames.txt", "r") as fi:
    for i in fi:
        i = i.replace("\n", "")
        bk.append(i)
        # print(i)

for i in range(1000000):
    amaze_me = ran.choice(bk)

sys(f"open '{amaze_me}'")
