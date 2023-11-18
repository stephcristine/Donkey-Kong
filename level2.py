import os
import WConio2 as WConio2
import cursor

class Fase2():

  def __init__(self):
    self.wall = "█"
    self.floor = "▀"
    self.roof = "▄"

    self.plat = '\033[1;31;40m⊠\033[m'
    self.platI = 0
    self.platJ = 0

    b = "\u001b[38;5;19m█"
    w = '\033[37m█\033[m'
    self.oil = [
        (b + b + b + b +  b + b + b + b),
        (b + w + w + w + w + w + w + b),
        (b + b + b + b +  b + b + b + b),
        (b + w + w + w + w + w + w + b),
        (b + b + b + b +  b + b + b + b)
      ]
    
    self.voce = '$'
    self.voceI = 10
    self.voceJ = 2

    self.simbolo = ''
    os.system('cls')
    cursor.hide()

  def draw_plat(self,x,y):
    self.platJ = x
    self.platI = y
    
    if self.platI == 6 and self.platJ >= 55 and self.platJ <= 95:
          print(self.plat, end='')
    elif self.platI == 12 and self.platJ >= 5 and self.platJ <= 144:
          print(self.plat, end='') 
    elif self.platI == 22 and self.platJ >= 0 and self.platJ <= 66:
        print(self.plat, end='')    
    elif self.platI == 22 and self.platJ >= 84 and self.platJ <= 150:
       print(self.plat, end='')  
    elif self.platI == 32 and self.platJ >= 0 and self.platJ <= 35:
      print(self.plat, end='')
    elif self.platI == 32 and self.platJ >= 55 and self.platJ <= 95:
       print(self.plat, end='')
    elif self.platI == 32 and self.platJ >= 115 and self.platJ <= 150:
      print(self.plat, end='')
    elif self.platI == 42 and self.platJ >= 5 and self.platJ <= 144:
      print(self.plat, end='')
    elif self.platI == 51 and self.platJ  >= 0 and self.platJ <= 150:
      print(self.plat, end='')
    else:
       print(" ", end='')

  def draw_oil(self,j,i):

        if (j==71):    #prints 
          if (i==22 ):
              print(self.oil[0], end='')
          if (i==23 ):
              print(self.oil[1], end='')
          if (i==24):
              print(self.oil[2], end='')
          if (i==25):
              print(self.oil[3], end='')
          if (i==26):
            print(self.oil[4], end='')

  def collision(self):

    if self.voceI == 6 and self.voceJ >= 55 and self.voceJ <= 95:
      self.voceI -= 1
    if self.voceI == 12 and self.voceJ >= 5 and self.voceJ <= 144:
      self.voceI -= 1
    if self.voceI == 22 and self.voceJ >= 0 and self.voceJ <= 66: 
      self.voceI -= 1
    elif self.voceI == 22 and self.voceJ >= 84 and self.voceJ <= 150:
      self.voceI -= 1
    if self.voceI == 32 and self.voceJ >= 0 and self.voceJ <= 35:
      self.voceI -= 1
    elif self.voceI == 32 and self.voceJ >= 55 and self.voceJ <= 95:
      self.voceI -= 1
    elif self.voceI == 32 and self.voceJ >= 115 and self.voceJ <= 150:
      self.voceI -= 1
    if self.voceI == 42 and self.voceJ >= 5 and self.voceJ <= 144:
       self.voceI -= 1
    if self.voceI == 51 and self.voceJ >= 0 and self.voceJ <= 150:
      self.voceI -= 1

    return self.voceJ, self.voceI
  
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
            self.voceI -= 2

      return self.voceI, self.voceJ

  def draw_screen(self):

    WConio2.gotoxy(0,0)
    #if self.platI >= self.voceI + 3 and self.cont % 60 == 0:
    #  self.voceI += 1
    print(self.roof * 152)
    for i in range(52):
        print(self.wall, end='')

        for j in range(150):
           
            if i==self.voceI and j==self.voceJ:
                print(self.voce, end='')
                self.voceJ, self.voceI = self.collision()
            else:
                self.draw_plat(j,i)
                self.draw_oil(j,i)
                
        print(self.wall)

        self.interaction()

    #print(life)
    print(self.floor * 152)