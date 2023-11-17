from fases import Fase1
from f import Fase2
from points import Points

game1 = Fase1()
#game2 = Fase2()

teste = Points(game1)



play = True
while play:
  game1.draw_screen() 
  teste.lose_life()
  #game2.draw_screen() 