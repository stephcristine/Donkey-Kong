import os
import WConio2 as WConio2
import cursor

class Fase1():
  def __init__(self,next_level,play):
    self.play = True
    self.next_level = False

    self.voce = '\033[1;34;40m█\033[m'
    self.voceI = 10
    self.voceJ = 2

    self.princess = "\u001b[38;5;200m█"
    self.princessI = 7     
    self.princessJ = 51
    self.contP = 0 
    self.moving = True

    self.plat = '\033[1;31;40m⊠\033[m'
    self.platI = 0
    self.platJ = 0

    self.wall ='\033[37m█\033[m'
    self.floor ='\033[37m▀\033[m'
    self.roof ='\033[37m▄\033[m'

    self.barril = "\u001b[38;5;179m▄"
    self.barril2 = "▄"
    self.barrilI = 14
    self.barrilJ = 1

    self.stairs = '\033[37mH\033[m'
    self.stairsI = 0
    self.stairsJ = 0

    self.cont = 0
    self.contB = 0

    self.score = 0
    self.coin = "\u001b[38;5;198m♦"  
    self.catch = [False,False,False,False,False,False,False]
    self.coinI = 0
    self.coinJ = 0

    self.climb = 0

    self.simbolo = ''

    os.system('cls')
    cursor.hide()

  def draw_elements(self,x,y):
    self.platJ = x
    self.platI = y
    self.stairsJ = x
    self.stairsI = y 
    self.coinJ = x
    self.coinI = y
    #platforms
    if self.platI == 8 and self.platJ >= 50 and self.platJ <= 100:
       print(self.plat, end='')
    elif self.platI == 15 and self.platJ >= 0 and self.platJ <=120:
        print(self.plat, end='')
    elif self.platI == 22 and self.platJ >= 30 and self.platJ<=150:
        print(self.plat, end='')
    elif self.platI == 29 and self.platJ >= 0 and self.platJ <=120:
        print(self.plat, end='')
    elif self.platI == 36 and self.platJ >= 30 and self.platJ <=150:
        print(self.plat, end='')
    elif self.platI == 43 and self.platJ >= 0 and self.platJ <=120:
        print(self.plat, end='')
    elif self.platI == 50 and self.platJ >= 0 and self.platJ <=150:
        print(self.plat, end='')
    #stairs
    elif self.stairsJ == 90 and self.stairsI >= 9 and self.stairsI <= 14:
       print(self.stairs,end='')  
    elif self.stairsJ == 110 and self.stairsI >= 16 and self.stairsI <= 21:
        print(self.stairs,end='')
    elif self.stairsJ == 40 and self.stairsI >= 23 and self.stairsI <= 28:
        print(self.stairs,end='')
    elif self.stairsJ == 100 and self.stairsI >= 30 and self.stairsI <= 35:
        print(self.stairs,end='')
    elif self.stairsJ == 45 and self.stairsI >= 37 and self.stairsI <= 42:
        print(self.stairs,end='')
    elif self.stairsJ == 119 and self.stairsI >= 44 and self.stairsI <= 49:
        print(self.stairs,end='')
    #coins
    elif self.coinI == 14 and self.coinJ == 10 and self.catch[0] == False:
      print(self.coin, end='')
      if self.catch[0] == True:
         print(" ",end='')
    elif self.coinI == 18 and self.coinJ == 125 and self.catch[1] == False:
      print(self.coin, end='')
      if self.catch[1] == True:
         print(" ",end='')
    elif self.coinI == 24 and self.coinJ == 35 and self.catch[2] == False:
      print(self.coin, end='')
      if self.catch[2] == True:
         print(" ",end='')
    elif self.coinI == 28 and self.coinJ == 124 and self.catch[3] == False:
      print(self.coin, end='')
      if self.catch[3] == True:
         print(" ",end='')
    elif self.coinI == 34 and self.coinJ == 140 and self.catch[4] == False:
      print(self.coin, end='')
      if self.catch[4] == True:
         print(" ",end='')
    elif self.coinI == 41 and self.coinJ == 5 and self.catch[5] == False:
      print(self.coin, end='')
      if self.catch[5] == True:
         print(" ",end='')
    elif self.coinI == 49 and self.coinJ == 141 and self.catch[6] == False:
      print(self.coin, end='')
      if self.catch[6] == True:
         print(" ",end='')
    else:
        print(' ', end='')  
        
  def move_barrel_Y(self):

    if self.barrilI >= 0 and self.barrilI < 14 and self.barrilJ >= 1:    
        self.barrilI += 1
    if self.barrilI >= 14 and self.barrilI < 21 and self.barrilJ >= 130 :
        self.barrilI += 1
    if self.barrilI >= 21 and self.barrilI < 28 and self.barrilJ <= 10 :
        self.barrilI += 1
    if self.barrilI >= 28 and self.barrilI < 35 and self.barrilJ >= 130:
        self.barrilI += 1
    if self.barrilI >= 35 and self.barrilI < 42 and self.barrilJ <= 10 :
        self.barrilI += 1
    if self.barrilI >= 42 and self.barrilI < 49 and self.barrilJ >= 130 :
        self.barrilI += 1  

    return self.barrilJ,self.barrilI
  
  def move_barrel_X(self):

    if self.barrilI == 14 and self.barrilJ >= 0 and self.barrilJ <= 130:
        if self.contB % 6 == 0:
            self.barrilJ += 1
    if self.barrilI == 21 and self.barrilJ >= 10 and self.barrilJ <= 131:
        if self.contB % 6 == 0:
            self.barrilJ -= 1
    if self.barrilI == 28 and self.barrilJ >= 0 and self.barrilJ <= 130:
        if self.contB % 6 == 0:
            self.barrilJ += 1
    if self.barrilI == 35 and self.barrilJ >= 10 and self.barrilJ <= 131:
        if self.contB % 6 == 0:
            self.barrilJ -= 1
    if self.barrilI == 42 and self.barrilJ >= 0 and self.barrilJ <= 130:
        if self.contB % 6 == 0:
            self.barrilJ += 1
    if self.barrilI == 49 and self.barrilJ >= 0 and self.barrilJ <= 131:
        if self.contB % 6 == 0:
            self.barrilJ -= 1

    if self.barrilI == 49 and self.barrilJ == 0:
       self.barrilI = 7
       self.barrilJ = 1

    return self.barrilJ,self.barrilI

  def move_princess(self):
      
    if self.princessI == 7 and self.princessJ >= 51 and self.princessJ <= 61 and self.moving == True:
      if self.contP % 15 == 0:
        self.princessJ += 1
        if self.princessJ == 62:
            self.moving = False
    if self.princessI == 7 and self.princessJ >= 51 and self.princessJ <= 62 and self.moving == False:
      if self.contP % 15 == 0:
        self.princessJ -= 1
        if self.princessJ == 51:
            self.moving = True
    
    return self.princessJ, self.moving

  def collision(self):
    
    if self.platI == 8 and self.platJ >= 49 and self.platJ <= 99 and self.climb == 0:
       self.voceI -= 1
    if self.voceI == 15 and self.voceJ >= 0 and self.voceJ <= 120 and self.climb == 0:
        self.voceI -= 1
    if self.voceI == 22 and self.voceJ >= 30 and self.voceJ <= 150 and self.climb == 0:
        self.voceI -= 1
    if self.voceI == 29 and self.voceJ >= 0 and self.voceJ <= 120 and self.climb == 0:
        self.voceI -= 1
    if self.voceI == 36 and self.voceJ >= 30 and self.voceJ <= 150 and self.climb == 0:
        self.voceI -= 1
    if self.voceI == 43 and self.voceJ >= 0 and self.voceJ <= 120 and self.climb == 0:
        self.voceI -= 1
    if self.voceI == 50 and self.voceJ >= 0 and self.voceJ <= 150 and self.climb == 0:
        self.voceI -= 1

    if self.voceJ == 90 and self.voceI >= 7 and self.voceI <= 15:
        self.climb = 1
    elif self.voceJ == 110 and self.voceI >= 14 and self.voceI <= 21:
        self.climb = 1
    elif self.voceJ == 40 and self.voceI >= 21 and self.voceI <= 28:
        self.climb = 1
    elif self.voceJ == 100 and self.voceI >= 28 and self.voceI <= 35:
        self.climb = 1
    elif self.voceJ == 45 and self.voceI >= 35 and self.voceI <= 42:
        self.climb = 1
    elif self.voceJ == 119 and self.voceI >= 42 and self.voceI <= 49:
        self.climb = 1
    else:
        self.climb = 0

    if self.voceI == self.barrilI and self.voceJ == self.barrilJ:
       self.play = False
   
    return self.voceJ, self.voceI, self.climb, self.play
  
  def points(self):
     
    if self.voceI == 14 and self.voceJ == 10 and self.catch[0] == False:
      self.score += 10
      self.catch[0] = True
    elif self.voceI == 18 and self.voceJ == 125 and self.catch[1] == False:
      self.score += 10
      self.catch[1] = True
    elif self.voceI == 24 and self.voceJ == 35 and self.catch[2] == False:
      self.score += 10
      self.catch[2] = True
    elif self.voceI == 28 and self.voceJ == 124 and self.catch[3] == False:
      self.score += 10
      self.catch[3] = True
    elif self.voceI == 34 and self.voceJ == 140 and self.catch[4] == False:
      self.score += 10
      self.catch[4] = True
    elif self.voceI == 41 and self.voceJ == 5 and self.catch[5] == False:
      self.score += 10
      self.catch[5] = True
    elif self.voceI == 49 and self.voceJ == 141 and self.catch[6] == False:
      self.score += 10
      self.catch[6] = True

    if self.voceI == self.princessI and self.voceJ == self.princessJ:
       self.next_level = True

    return self.score, self.catch, self.next_level

  def gravity(self):
    if self.platI >= self.voceI + 3 and self.cont % 60 == 0 and self.climb == 0:
        self.voceI += 1

    return self.voceI

  def interaction(self):
    if WConio2.kbhit():
      (tecla, self.simbolo) = WConio2.getch()
      if self.simbolo == 'a' or self.simbolo == 'A':
          self.voceJ -= 1
      if self.simbolo == 'd' or self.simbolo == 'D':
          self.voceJ += 1
      if self.simbolo == 's' or self.simbolo == 'S':
          self.voceI += 1
      if self.simbolo == ' ':
          self.voceI -= 3
      
      if self.voceJ == 90 and self.voceI >= 8 and self.voceI <= 14 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 110 and self.voceI >= 15 and self.voceI <= 21 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 40 and self.voceI >= 22 and self.voceI <= 28 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 100 and self.voceI >= 29 and self.voceI <= 35 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 45 and self.voceI >= 36 and self.voceI <= 42 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 119 and self.voceI >= 43 and self.voceI <= 49 and self.simbolo == 'w':
        self.voceI -= 1

    return self.voceI, self.voceJ

  def draw_screen(self):

    WConio2.gotoxy(0,0)
    self.gravity()
    self.interaction()  
    print(self.roof * 152)
    for i in range(52):
        print(self.wall, end='')
        
        for j in range(150):

            if i == self.barrilI and j == self.barrilJ:
                print(self.barril, end='')
                self.contB += 1
                self.barrilJ, self.barrilI = self.move_barrel_X()
            elif i == self.voceI and j == self.voceJ:
                print(self.voce, end='')
                self.voceJ, self.voceI, self.climb, self.play = self.collision()   
            elif i == self.princessI and j == self.princessJ:
                print(self.princess, end='')
                self.contP += 1
                self.move_princess()
            else:
                self.draw_elements(j,i)  
                self.score,self.catch, self.next_level = self.points()

        print(self.wall)
        self.cont += 1

        if self.cont % 10 == 0:
           self.barrilJ, self.barrilI = self.move_barrel_Y()
            
    print(self.floor * 152)
    print("      SCORE  =  ",self.score)