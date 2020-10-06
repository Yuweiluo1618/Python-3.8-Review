import time
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

w.addch(int(sh/2), int(sw/2), curses.ACS_PI)
s.clear()