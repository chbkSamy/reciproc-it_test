import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
liste = list()
petit_ecart = float('inf')

for i in range(n):
    pi = int(input())
    if i == 0:
        liste.append(pi)
    else:
        for j in range(i):
            if pi < liste[j]:
                liste.insert(j, pi)
                break
        else:
            liste.append(pi)

for i in range(1, len(liste)):
    if liste[i] - liste[i - 1] < petit_ecart:
        petit_ecart = liste[i] - liste[i - 1]

print(petit_ecart)

#lien coding game: https://www.codingame.com/training/easy/horse-racing-duals/solution

