import os
import cursor
import WConio2 as WConio2
from home_screen import home_screen
from high_scores import high_scores
from level1 import Fase1
from level2 import Fase2


os.system('cls')
cursor.hide()

arrow_position = 42
cont = 0
go_to = 0

while True:
    
    WConio2.gotoxy(0, 0)

    if cont == 0 or go_to==1:
        if(arrow_position==1):
            os.system('cls')
            arrow_position=42
        go_to=0
        cont=0
        arrow_position = home_screen(arrow_position)
        print(arrow_position)
    
    if (arrow_position == 0):
        if cont==1:
            go_to = Fase1()
            go_to.draw_screen()
        cont = 1
    if (arrow_position == 1 ):
        if cont==2:
            go_to = high_scores()
        cont = 2
          
        
# import os
# import cursor
# import WConio2 as WConio2
# from home_screen import home_screen
# from high_scores import high_scores


# os.system('cls')
# cursor.hide()

# arrow_position = 42
# cont = 0
# go_to = 0

# while True:

#     WConio2.gotoxy(0, 0)

#     if cont == 0 or go_to==1:
#         if(arrow_position==0):
#             os.system('cls')
#             arrow_position=42
#         go_to=0
#         cont=0
#         arrow_position = home_screen(arrow_position)
#         print(arrow_position)
#     if (arrow_position == 0 ):
#         if cont==1:
#             go_to = high_scores()
#         cont = 1