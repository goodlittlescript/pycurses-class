import os

lines = [
    ".X.......",
    "..X......",
    "...X.....",
    "....X....",
    ".....X...",
    "......X..",
    ".......X.",
    "......X..",
    ".....X...",
    "....X....",
    "...X.....",
    "..X......",
    ".X.......",
]

for line in lines:
    os.system("clear")
    print(line)
    input()