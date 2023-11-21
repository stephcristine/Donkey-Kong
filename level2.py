import os
import WConio2 as WConio2
import cursor

os.system('cls')
cursor.hide()

class Fase2():

  def __init__(self,end,play):

    self.the_end = False

    self.princess = "\u001b[38;5;200m█"
    self.princessI = 5     
    self.princessJ = 56
    self.contP = 0 
    self.moving = True

    self.wall = '\033[37m█\033[m'    
    self.floor = '\033[37m▀\033[m'      
    self.roof = '\033[37m▄\033[m'

    self.plat = "\u001b[38;5;214m⊠"
    self.platI = 0    
    self.platJ = 0

    b = '\u001b[38;5;19m█'
    w = '\033[37m█\033[m'
    dw = "\u001b[38;5;231m▄"
    self.oil = [
        (b + b + b + b +  b + b + b + b),
        (b + w + w + w + w + w + w + b),
        (b + b + b + b +  b + b + b + b),
        (b + w + w + w + w + w + w + b),
        (b + b + b + b +  b + b + b + b)
      ]
    
    self.voce = '\033[1;34;40m█\033[m'
    self.voceI = 50
    self.voceJ = 5
    self.is_plat_true = False
    self.is_oil_true = False
    self.stairs ="\u001b[38;5;19mH"
    self.stairsI = 0
    self.stairsJ = 0
    self.climb = 0
    self.max_score = 1000
    self.max_timing = 600
    self.timing=0
    self.timing= min(self.timing, self.max_score)
    self.factor_time = 0.8
    self.cont = 0
    self.barril = "\u001b[38;5;179m▄"
    self.barril2 = "\u001b[38;5;179m▄"
    self.barrilJ = 0
    self.barrilI = 31
    self.contB = 0
    self.barrilJ2 = 102
    self.barrilI2 = 31
    self.contB2 = 0
    self.barrilJ3 = 8
    self.barrilI3 = 11
    self.contB3 = 0
    self.barrilJ4 = 8
    self.barrilI4 = 41
    self.contB4 = 0
    self.play = True
    self.score = 0

    self.coin = "\u001b[38;5;198m♦" 
    self.is_coin_true = [True, True, True, True, True, True, True, True]

    self.simbolo = ''

  def draw_plat(self,x,y):
    self.platJ = x
    self.platI = y
    self.stairsJ = x
    self.stairsI = y    
    self.oilJ = x
    self.oilI = y
    self.coinJ = x
    self.coinI = y

    #Print platforms

    if self.platI == 6 and self.platJ >= 55 and self.platJ <= 95:
          print(self.plat, end='')
    elif self.platI == 12 and self.platJ >= 5 and self.platJ <= 144:
          print(self.plat, end='') 
    elif self.platI == 22 and self.platJ >= 0 and self.platJ <= 150:
        print(self.plat, end='')  
    elif self.platI == 32 and self.platJ >= 0 and self.platJ <= 50:
      print(self.plat, end='')
    elif self.platI == 32 and self.platJ >= 55 and self.platJ <= 95:
       print(self.plat, end='')
    elif self.platI == 32 and self.platJ >= 100 and self.platJ <= 150:
      print(self.plat, end='')
    elif self.platI == 42 and self.platJ >= 5 and self.platJ <= 144:
      print(self.plat, end='')
    elif self.platI == 51 and self.platJ  >= 0 and self.platJ <= 150:
      print(self.plat, end='')
    
    #Print stairs
      
    elif self.stairsJ == 90 and self.stairsI >= 7 and self.stairsI <= 11:
      print(self.stairs,end='')
    elif self.stairsJ == 30 and self.stairsI >= 13 and self.stairsI <= 21:
        print(self.stairs,end='')
    elif self.stairsJ == 120 and self.stairsI >= 13 and self.stairsI <= 21:
        print(self.stairs,end='')
    elif self.stairsJ == 60 and self.stairsI >= 22 and self.stairsI <= 31:
        print(self.stairs,end='')
    elif self.stairsJ == 90 and self.stairsI >= 22 and self.stairsI <= 32:
        print(self.stairs,end='')
    elif self.stairsJ == 120 and self.stairsI >= 33 and self.stairsI <= 41:
        print(self.stairs,end='')
    elif self.stairsJ == 30 and self.stairsI >= 33 and self.stairsI <= 41:
        print(self.stairs,end='')
    elif self.stairsJ == 20  and self.stairsI >= 43 and self.stairsI <= 50:
        print(self.stairs,end='')  
    elif self.stairsJ == 130 and self.stairsI >= 43 and self.stairsI <= 50:
        print(self.stairs,end='')   

    elif self.coinI == 31 and self.coinJ == 50 and self.is_coin_true[0]==True:
      print(self.coin, end='')
    elif self.coinI == 41 and self.coinJ == 130 and self.is_coin_true[1]==True:
      print(self.coin, end='')
    elif self.coinI == 41 and self.coinJ == 80 and self.is_coin_true[2]==True:
      print(self.coin, end='')
    elif self.coinI == 11 and self.coinJ == 77 and self.is_coin_true[3]==True:
      print(self.coin, end='')
    elif self.coinI == 21 and self.coinJ == 50 and self.is_coin_true[4]==True:
      print(self.coin, end='')
    elif self.coinI == 21 and self.coinJ == 92 and self.is_coin_true[5]==True:
      print(self.coin, end='')
    elif self.coinI == 31 and self.coinJ == 141 and self.is_coin_true[6]==True:
      print(self.coin, end='')
    elif self.coinI == 50 and self.coinJ == 50 and self.is_coin_true[7]==True:
      print(self.coin, end='')
    else:
       print(" ", end='')

  def move_barrel_X(self):

    if self.barrilI == 31 and self.barrilJ >= 0 and self.barrilJ <= 48:
        if self.contB % 3 == 0:
          if self.barrilJ == 48:
              self.direction = -1
          elif self.barrilJ == 0:
              self.direction = 1

          self.barrilJ += self.direction
        return self.barrilJ,self.barrilI
    
  def move_barrel_X2(self):
     
    if self.barrilI2 == 31 and self.barrilJ2 >= 102 and self.barrilJ2 <= 150:
        if self.contB2 % 3 == 0:
          if self.barrilJ2 == 148:
              self.direction2 = -1
          if self.barrilJ2 ==102:
              self.direction2 = 1

          self.barrilJ2 += self.direction2
    return self.barrilJ2,self.barrilI2

  def move_barrel_X3(self):
     
    if self.barrilI3 == 11 and self.barrilJ3 >= 8 and self.barrilJ3 <= 141:
        if self.contB3 % 2 == 0:
          if self.barrilJ3 == 141:
              self.direction3 = -1
          if self.barrilJ3 ==8:
              self.direction3 = 1

          self.barrilJ3 += self.direction3
    return self.barrilJ3,self.barrilI3

  def move_barrel_X4(self):
    
    if self.barrilI4 == 41 and self.barrilJ4 >= 8 and self.barrilJ4 <= 141:
        if self.contB4 % 2 == 0:
          if self.barrilJ4 == 141:
              self.direction4 = -1
          if self.barrilJ4 ==8:
              self.direction4 = 1

          self.barrilJ4 += self.direction4
    return self.barrilJ4,self.barrilI4

  def move_princess(self):

      if self.princessI == 7 and self.princessJ >= 56 and self.princessJ <= 66 and self.moving == True:
        if self.contP % 15 == 0:
          self.princessJ += 1
          if self.princessJ == 67:
              self.moving = False
      if self.princessI == 7 and self.princessJ >= 56 and self.princessJ <= 67 and self.moving == False:
        if self.contP % 15 == 0:
          self.princessJ -= 1
          if self.princessJ == 56:
              self.moving = True

      return self.princessJ, self.moving

  def collision(self):

    if self.voceI == 6 and self.voceJ >= 55 and self.voceJ <= 95 and self.climb ==0:
      self.voceI -= 1
    if self.voceI == 12 and self.voceJ >= 5 and self.voceJ <= 144 and self.climb ==0:
      self.voceI -= 1
    if self.voceI == 22 and self.voceJ >= 0 and self.voceJ <= 150 and self.climb ==0: 
      self.voceI -= 1
    if self.voceI == 32 and self.voceJ >= 0 and self.voceJ <= 50 and self.climb ==0:
      self.voceI -= 1
    elif self.voceI == 32 and self.voceJ >= 55 and self.voceJ <= 95 and self.climb ==0:
      self.voceI -= 1
    elif self.voceI == 32 and self.voceJ >= 100 and self.voceJ <= 150 and self.climb ==0:
      self.voceI -= 1
    if self.voceI == 42 and self.voceJ >= 5 and self.voceJ <= 144 and self.climb ==0:
       self.voceI -= 1
    if self.voceI == 51 and self.voceJ >= 0 and self.voceJ <= 150 and self.climb ==0:
      self.voceI -= 1

    if self.voceJ == 90 and self.voceI >= 7 and self.voceI <= 11:
        self.climb = 1
    elif self.voceJ == 30 and self.voceI >= 13 and self.voceI <= 21:
        self.climb = 1
    elif self.voceJ == 120 and self.voceI >= 13 and self.voceI <= 21:
        self.climb = 1
    elif self.voceJ == 60 and self.voceI >= 22 and self.voceI <= 31:
        self.climb = 1
    elif self.voceJ == 90 and self.voceI >= 22 and self.voceI <= 32:
        self.climb = 1
    elif self.voceJ == 120 and self.voceI >= 33 and self.voceI <= 41:
        self.climb = 1
    elif self.voceJ == 30 and self.voceI >= 33 and self.voceI <= 41:
        self.climb = 1
    elif self.voceJ == 20  and self.voceI >= 43 and self.voceI <= 50:
        self.climb = 1
    elif self.voceJ == 130 and self.voceI >= 43 and self.voceI <= 50:
        self.climb = 1
    else:
        self.climb = 0

    if self.voceI == 31 and self.voceJ == 50 and self.is_coin_true[0]==True:
      self.score +=10
      self.is_coin_true[0]= False
    elif self.voceI == 41 and self.voceJ == 130 and self.is_coin_true[1]==True:
      self.score +=10
      self.is_coin_true[1]= False
    elif self.voceI == 41 and self.voceJ == 80 and self.is_coin_true[2]==True:
      self.score +=10
      self.is_coin_true[2]= False
    elif self.voceI== 11 and self.voceJ == 77 and self.is_coin_true[3]==True:
      self.score +=10
      self.is_coin_true[3]= False
    elif self.voceI == 21 and self.voceJ == 50 and self.is_coin_true[4]==True:
      self.score +=10
      self.is_coin_true[4]= False
    elif self.voceI == 21 and self.voceJ == 92 and self.is_coin_true[5]==True:
      self.score +=10
      self.is_coin_true[5]= False
    elif self.voceI == 31 and self.voceJ == 141 and self.is_coin_true[6]==True:
      self.score +=10
      self.is_coin_true[6]= False
    elif self.voceI == 50 and self.voceJ== 50 and self.is_coin_true[7]==True:
      self.score +=10
      self.is_coin_true[7]= False

    if self.voceI == self.barrilI and self.voceJ == self.barrilJ:
       self.play = False
    if self.voceI == self.barrilI2 and self.voceJ == self.barrilJ2:
       self.play = False
    if self.voceI == self.barrilI3 and self.voceJ == self.barrilJ3:
       self.play = False
    if self.voceI == self.barrilI4 and self.voceJ == self.barrilJ4:
       self.play = False       

    if self.voceI == self.princessI and self.voceJ == self.princessJ:
        self.the_end = True

    return self.voceJ, self.voceI, self.climb, self.play, self.score, self.is_coin_true, self.the_end
  
  def interaction(self):
      if WConio2.kbhit():
        (tecla, self.simbolo) = WConio2.getch()
        if self.simbolo == 'a' or self.simbolo == 'A':
            self.voceJ -= 1
        elif self.simbolo == 'd' or self.simbolo == 'D':
            self.voceJ += 1
        elif self.simbolo == 's' or self.simbolo == 'S':
            self.voceI += 1
        if self.simbolo == ' ':
            self.voceI -= 3

      if self.voceJ == 90 and self.voceI >= 7 and self.voceI <= 11 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 30 and self.voceI >= 13 and self.voceI <= 21 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 120 and self.voceI >= 13 and self.voceI <= 21 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 60 and self.voceI >= 22 and self.voceI <= 31 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 90 and self.voceI >= 22 and self.voceI <= 32 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 120 and self.voceI >= 33 and self.voceI <= 41 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 30 and self.voceI >= 33 and self.voceI <= 41 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 20  and self.voceI >= 43 and self.voceI <= 50 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 130 and self.voceI >= 43 and self.voceI <= 50 and self.simbolo == 'w':
          self.voceI -= 1

      return self.voceI, self.voceJ

  def gravity(self):
    if self.platI >= self.voceI and self.cont % 15 == 0 and self.climb == 0:
        self.voceI += 1

    return self.voceI
  
  def high_scores_file(self, fase1_score, fase2_score):
    if not self.play:
        total_score = fase1_score + fase2_score
        with open("high_scores.txt", "a") as scores:
            scores.write(f'  =  {total_score}')

  def draw_screen(self):

    WConio2.gotoxy(0,0)
    self.gravity()
    print(self.roof * 152)
    for i in range(52):
        print(self.wall, end='')

        for j in range(150):
            if i == self.barrilI and j == self.barrilJ:
                print(self.barril, end='')
                self.contB += 1
                self.barrilJ, self.barrilI = self.move_barrel_X()
            elif i == self.barrilI2 and j == self.barrilJ2:
                print(self.barril, end='')
                self.contB2 += 1
                self.barrilJ2, self.barrilI2 = self.move_barrel_X2()
            elif i == self.barrilI3 and j == self.barrilJ3:
                print(self.barril, end='')
                self.contB3 += 1
                self.barrilJ3, self.barrilI3 = self.move_barrel_X3()
            elif i == self.barrilI4 and j == self.barrilJ4:
                print(self.barril, end='')
                self.contB4 += 1
                self.barrilJ4, self.barrilI4 = self.move_barrel_X4()
            elif i==self.voceI and j==self.voceJ:
                print(self.voce, end='')
                self.voceJ, self.voceI, self.climb, self.play, self.score, self.is_coin_true, self.the_end = self.collision()
            elif i == self.princessI and j == self.princessJ:
                print(self.princess, end='')
                self.contP += 1
                self.move_princess()
            else:
                self.draw_plat(j,i)

        print(self.wall)
        self.cont += 1
        if self.cont % 10 == 0:
          self.interaction()
        self.high_scores_file(1,2)

    print(self.floor * 152)
    print("                      SCORE  =  ",self.score)