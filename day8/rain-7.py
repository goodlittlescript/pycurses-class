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
    "l": "right",
    " ": "drop",
    "q": "quit",
}


class Raindrop:
    def __init__(self, y_location, x_location):
        self.y_location = y_location
        self.x_location = x_location


def main(stdscr):
    stdscr.nodelay(True)
    max_y, max_x = stdscr.getmaxyx()

    now = 0
    y_location = 0
    x_location = 0
    ground = max_y - 1
    raindrops = []

    debug = (
        f"now: {now} ({y_location:.0f}, {x_location:.0f}) raindrops: {len(raindrops)}"
    )
    stdscr.addstr(ground, 0, debug.ljust(max_x - 1, " "))
    stdscr.move(int(y_location), int(x_location))
    stdscr.refresh()

    while True:
        time.sleep(0.1)
        try:
            key = stdscr.getkey()
        except Exception:
            key = ""
        cmd = keymap.get(key, "unknown")

        if cmd == "left":
            x_location -= 1
        if cmd == "right":
            x_location += 1
        if cmd == "quit":
            exit()
        if cmd == "unknown":
            pass

        y_location = bound_location(y_location, 0, max_y)
        x_location = bound_location(x_location, 0, max_x)
        now += 1

        if cmd == "drop":
            raindrop = Raindrop(y_location, x_location)
            raindrops.append(raindrop)

        for raindrop in raindrops:
            stdscr.addstr(raindrop.y_location, raindrop.x_location, " ")

        new_raindrops = []
        for raindrop in raindrops:
            raindrop.y_location += 1
            if raindrop.y_location < ground:
                new_raindrop = Raindrop(raindrop.y_location, raindrop.x_location)
                new_raindrops.append(new_raindrop)

        for raindrop in new_raindrops:
            stdscr.addstr(raindrop.y_location, raindrop.x_location, ".")

        raindrops = new_raindrops

        debug = f"now: {now} ({y_location:.0f}, {x_location:.0f}) raindrops: {len(raindrops)}"
        stdscr.addstr(ground, 0, debug.ljust(max_x - 1, " "))
        stdscr.move(int(y_location), int(x_location))
        stdscr.refresh()


curses.wrapper(main)
