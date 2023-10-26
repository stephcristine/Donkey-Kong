#import os
#import WConio2 as WConio2
#import cursor

class Fase1():
    def __init__(self, princess, gorilla, coins, plumber):
        self.p = princess
        self.g = gorilla
        self.c = coins
        self.p = plumber
        self.plat = '\033[1;31;40m=\033[m'
        self.roof = "▄"
        self.wall = "█"
        self.ground = "▀"

    def platform(self):
        self.i = 0
        self.j = 0 
    
        print(self.roof * 152)
        for self.i in range(52):
            print(self.wall, end='')
            for self.j in range(150):
                if self.i == 4 and self.j >= 50 and self.j <= 100:
                   print(self.plat, end='')
                elif self.i == 10 and self.j>= 0 and self.j <=120:
                    print(self.plat, end='')
                elif self.i == 18 and self.j>= 30 and self.j <=150:
                    print(self.plat, end='')
                elif self.i == 26 and self.j>= 0 and self.j <=120:
                    print(self.plat, end='')
                elif self.i == 34 and self.j>= 30 and self.j <=150:
                    print(self.plat, end='')
                elif self.i == 42 and self.j>= 0 and self.j <=120:
                    print(self.plat, end='')
                elif self.i == 50 and self.j>= 0 and self.j <=150:
                    print(self.plat, end='')
                else:
                    print(" ", end='')
            print(self.wall) 
        print(self.ground * 152)

        return self.i, self.j 


teste = Fase1(1,2,3,4)

teste.platform()



