import os
import time
import sys

line = [":", ".", ".", ".", ".", ".", ".", ".", ":"]


def render(line, location):
    os.system("clear")
    for index, char in enumerate(line):
        if index == location:
            sys.stdout.write("X")
        else:
            sys.stdout.write(char)
    sys.stdout.write("\n")


location = 1
for _ in range(0, 39):
    render(line, location)

    location += 1
    if location > 7:
        location = 1

    time.sleep(0.1)
