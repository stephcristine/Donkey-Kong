import os
import cursor
import WConio2 as WConio2
import home_screen
import high_scores

while True:
    arrow_position = 42

    WConio2.gotoxy(0, 0)
    home_screen_result = home_screen.home_screen(arrow_position)
    if home_screen_result == 0:
        go_to = high_scores.high_scores()
        if go_to == 1:
            home_screen_result
            break
    elif home_screen_result == 1:
        break