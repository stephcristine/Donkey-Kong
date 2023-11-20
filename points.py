class Points():
  def __init__(self):
    self.bonus = 1000
    self.cont = 0
    self.total_points = 0
    self.coins = '\033[1;32;40m♦\033[m'
    self.coinI = 0
    self.coinJ = 0
    self.i = 0
    self.j = 0
    self.coin1 = [5,10]
    self.coin2 = [28,100]

    

  def bonus_points(self):
    for self.i in range(52):
       for self.j in range(150):
        if self.bonus > 0 and self.cont % 600 == 0:
            self.bonus -= 1
            print(self.bonus)
    self.cont += 1
    return self.bonus,self.i,self.j
  
  def draw_coins(self,x,y):
    self.coinI = y
    self.coinJ = x

    if self.coin1[0] == self.coinI and self.coin1[1] == self.coinJ:
      print(self.coins, end='')
    
    return self.coinI, self.coinJ     