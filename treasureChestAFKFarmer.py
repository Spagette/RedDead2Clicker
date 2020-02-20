import pyautogui as ag
import pygetwindow as gw
import time
import pymsgbox as mb

window_title = 'Red Dead Redemption 2'
rdr_2_win = gw.getWindowsWithTitle(window_title)[0]
rdr_2_win.activate()

win_pos = rdr_2_win.topleft
ag.moveTo(win_pos[0] + 1, win_pos[1] + 1)

waits = {
    # 'heirloomsWait': 42,
    # 'coinWait': 45,
    # # tarotWait = ?
    # 'bottleWait': 25,
    # 'arrowWait': 33,
    # 'braceletWait': 24,
    # 'earringWait': 26,
    'necklaceWait': 26,
    'ringWait': 35
}
# testWait = 1000
MAXSET = 7

time.sleep(1)

for wait in waits:
    for collector_set in range(0, MAXSET):
        rdr_2_win.activate()
        ag.keyDown('enter', 1)
        ag.keyUp('enter')
        rdr_2_win.activate()
        ag.keyDown('r', waits[wait])
        ag.keyUp('r', 1)

    if wait is not 'ringWait':
        if wait is 'coinWait':
            rdr_2_win.activate()
            ag.keyDown('down')
            ag.keyUp('down')
        rdr_2_win.activate()
        ag.keyDown('down')
        ag.keyUp('down')
    # TODO: set up movement so boxes dont overlap


# TODO: set up ctrl-c exit capability



