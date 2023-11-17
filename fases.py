import os
import WConio2 as WConio2
import cursor

class Fase1():
  def __init__(self):
    self.voce = '$'
    self.voceI = 10
    self.voceJ = 2

    self.plat = '\033[1;31;40m⊠\033[m'
    self.platI = 0
    self.platJ = 0

    self.teste = ''

    self.wall = "█"
    self.floor = "▀"
    self.roof = "▄"

    self.barril = "█"
    self.barrilI = 0
    self.barrilJ = 2

    self.stairs = "H"
    self.stairsI = 0
    self.stairsJ = 0

    self.cont = 0
    self.contB = 0

    self.play = 3

    self.climb = 0

    self.simbolo = ''

    os.system('cls')
    cursor.hide()

  def draw_plat(self,x,y):
    self.platJ = x
    self.platI = y
    
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
    else:   
        print(" ", end='')
        
  def draw_stairs(self,x,y):
      self.stairsJ = x
      self.stairsI = y
      
      if self.stairsJ == 90 and self.stairsI >= 9 and self.stairsI <= 14:
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

  def move_barrel_Y(self):

    if self.barrilI >= 0 and self.barrilI < 14 and self.barrilJ == 2:    
        self.barrilI += 1
    if self.barrilI >= 14 and self.barrilI <21 and self.barrilJ >= 130 :
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
    if self.barrilI == 49 and self.barrilJ >= 10 and self.barrilJ <= 131:
        if self.contB % 6 == 0:
            self.barrilJ -= 1

    return self.barrilJ,self.barrilI
  
  def collision(self):

    if self.voceI == 15 and self.voceJ >= 0 and self.voceJ <= 120:
        self.voceI -= 1
    if self.voceI == 22 and self.voceJ >= 30 and self.voceJ <= 150:
        self.voceI -= 1
    if self.voceI == 29 and self.voceJ >= 0 and self.voceJ <= 120:
        self.voceI -= 1
    if self.voceI == 36 and self.voceJ >= 30 and self.voceJ <= 150:
        self.voceI -= 1
    if self.voceI == 43 and self.voceJ >= 0 and self.voceJ <= 120:
        self.voceI -= 1
    if self.voceI == 50 and self.voceJ >= 0 and self.voceJ <= 150:
        self.voceI -= 1

    if self.voceJ == 90 and self.voceI >= 9 and self.voceI <= 15:
        print(self.stairs,end='')
        self.climb = 1
    elif self.voceJ == 110 and self.voceI >= 16 and self.voceI <= 21:
        print(self.stairs,end='')
        self.climb = 1
    elif self.voceJ == 40 and self.voceI >= 23 and self.voceI <= 28:
        print(self.stairs,end='')
        self.climb = 1
    elif self.voceJ == 100 and self.voceI >= 30 and self.voceI <= 35:
        print(self.stairs,end='')
        self.climb = 1
    elif self.voceJ == 45 and self.voceI >= 37 and self.voceI <= 42:
        print(self.stairs,end='')
        self.climb = 1
    elif self.voceJ == 119 and self.voceI >= 44 and self.voceI <= 49:
        print(self.stairs,end='')
        self.climb = 1
    else:
        self.climb = 0
   
    return self.voceJ, self.voceI, self.climb
  
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
          self.voceI -= 2
      
      if self.voceJ == 90 and self.voceI >= 9 and self.voceI <= 14 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 110 and self.voceI >= 16 and self.voceI <= 21 and self.simbolo == 'w':
          self.voceI -= 1
      if self.voceJ == 40 and self.voceI >= 23 and self.voceI <= 28 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 100 and self.voceI >= 30 and self.voceI <= 35 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 45 and self.voceI >= 37 and self.voceI <= 42 and self.simbolo == 'w':
        self.voceI -= 1
      if self.voceJ == 119 and self.voceI >= 44 and self.voceI <= 49 and self.simbolo == 'w':
        self.voceI -= 1

    return self.voceI, self.voceJ

  def draw_screen(self):

    WConio2.gotoxy(0,0)
    self.gravity()
    print(self.roof * 152)
    for i in range(52):
        print(self.wall, end='')
        
        for j in range(150):
            
            if i == self.barrilI and j == self.barrilJ:
                print(self.barril, end='' )
                self.contB += 1
                self.barrilJ, self.barrilI = self.move_barrel_X()
            elif i==self.voceI and j==self.voceJ:
                print(self.voce, end='')
                self.voceJ, self.voceI, self.climb = self.collision()
            else:
                self.draw_plat(j,i)
                self.draw_stairs(j,i)
        print(self.wall)
        self.cont += 1

        if self.cont % 10 == 0:
           self.barrilJ, self.barrilI = self.move_barrel_Y()
           self.interaction()

    print(self.climb)
    print(self.voceJ)
    print(self.floor * 152)