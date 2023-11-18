from level1 import Fase1

class Points():
  def __init__(self, play):
    self.bonus = 1000
    self.play = play
    self.cont = 0

  def bonus_points(self):
  
    for i in range(10):
      self.cont += 1
      if self.cont % 100 == 0:
        self.bonus -= 1
        if self.bonus == 900:
          break

    print(self.bonus)
    print(self.play)
    return self.play