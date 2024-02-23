import os
import curses
import time

# Bounds the location if it leaves the specified range.
#
# Note the range is [lower,upper) meaning it includes the
# lower value but only goes "up to" the upper value.
def bound_location(location, lower, upper):
    if location >= upper:
        return upper - 1
    elif location < lower:
        return lower
    else:
        return location

keymap = {
    "h": "left",
    "j": "down",
    "k": "up",
    "l": "right",
    "q": "quit",
}

def main(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    
    now = 0
    y_location = 0
    x_location = 0

    debug = f"now: {now} ({y_location}, {x_location})"
    stdscr.addstr(max_y-1, 0, debug.ljust(max_x - 1, " "))
    stdscr.move(y_location, x_location)
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        cmd = keymap.get(key, "unknown")

        y_curr, x_curr = stdscr.getyx()

        if cmd == "left":
            x_location -= 1
        if cmd == "right":
            x_location += 1
        if cmd == "up":
            y_location -= 1
        if cmd == "down":
            y_location += 1
        if cmd == "quit":
            exit()
        if cmd == "unknown":
            pass

        y_location = bound_location(y_location, 0, max_y)
        x_location = bound_location(x_location, 0, max_x)
        now += 1

        debug = f"now: {now} ({y_location}, {x_location})"
        stdscr.addstr(max_y-1, 0, debug.ljust(max_x - 1, " "))
        stdscr.move(y_location, x_location)
        stdscr.refresh()


curses.wrapper(main)
