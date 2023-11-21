import os
import cursor
import WConio2 as WConio2
from home_screen import home_screen
from high_scores import high_scores
from level2 import Fase2
from level1 import Fase1
from between_levels import between_levels_1
from end import last_screen


os.system('cls')
cursor.hide()

the_end = False
next_level = False
play1 = True
play2 = True

one = Fase1(next_level,play1)
two = Fase2(the_end, play2)

arrow_position = 42
cont = 0
go_to = 0

while one.play1 or two.play2:
    WConio2.gotoxy(0, 0)

    if cont == 0 or go_to==1:
        if(arrow_position==1):
            os.system('cls')
            arrow_position=42
        go_to=0
        cont=0
        arrow_position = home_screen(arrow_position)
    
    if arrow_position == 0 and one.next_level == False:
        if cont==1:
            go_to = one
            go_to.draw_screen()
        cont = 1
    if arrow_position == 1 :
        if cont==2:
            go_to = high_scores()
        cont = 2

    if one.play1 and one.next_level:
        two.draw_screen()
    
    if one.play1 == False or two.play2 == False:
        break