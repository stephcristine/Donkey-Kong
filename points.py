class Points():
  def __init__(self):
    self.bonus = 1000
    self.cont = 0
    self.total_points = 0
    self.coins = '\033[1;32;40m♦\033[m'
    

  def bonus_points(self):
    for i in range(10):
      self.cont += 1
      if self.cont % 100 == 0:
        if self.bonus > 0:
            self.bonus -= 1

    print(self.bonus)
    return self.bonus
  
  def draw_coins(self,x,y):
    i = y
    j = x
    self.coin1 = [20,130]
    self.coin2 = [28,123]
    self.coin3 = [39,50]

    if i == self.coin1[0] and j == self.coin1[1]:
      print(self.coins, end='')
    elif i == self.coin2[0] and j == self.coin2[1]:
      print(self.coins, end='')
    elif i == self.coin3[0] and j == self.coin3[1]:
      print(self.coins, end='')



    self.coinsI = [20,28,39]
    self.coinsJ = [130,123,50]