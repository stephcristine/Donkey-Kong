from fases import Fase1

class Points(Fase1):
  def __init__(self, game1):
    self.lifes = 3
    self.bonus = 1000
    self.testet = game1

  def lose_life(self):
    self.testet.collision()