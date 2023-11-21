import os
import cursor
import WConio2

# Color setting variables
g = "\u001b[38;5;34m█"  #green
r = "\u001b[38;5;124m█"  #red
y = "\u001b[38;5;214m█"  #yellow
upy = "\u001b[38;5;214m▀"  #yellow square up
dy = "\u001b[38;5;214m▄"  #yellow square down
b = "\u001b[38;5;19m█"  #blue
db = "\u001b[38;5;19m▄"  #blue small square down
upb = "\u001b[38;5;19m▀"  #blue small square down
lg = "\u001b[38;5;160m█"  #light red
w = "\u001b[38;5;231m█"  #white
upw = "\u001b[38;5;231m▀"  #white small square up
dw = "\u001b[38;5;231m▄"  #white small square down
o = "\u001b[38;5;202m█"  #orange
upo = "\u001b[38;5;202m▀"  #orange smalll square up
do = "\u001b[38;5;202m▄"  #orange smalll square down
lo = "\u001b[38;5;215m█"  #light orange
br = "\u001b[38;5;52m█"  #brown
dbr = "\u001b[38;5;52m▄"  #brown small square down
upbr = "\u001b[38;5;52m▀"  #brown small square up
lbr = "\u001b[38;5;179m█"  #light brow
uplbr = "\u001b[38;5;179m▀"  #light brown small square up
dlbr = "\u001b[38;5;179m▄"  #light brown small square down
mbr = "\u001b[38;5;88m█"  #mid brow
upmbr = "\u001b[38;5;88m▀"  #mid brown small square up
dmbr = "\u001b[38;5;88m▄"  #mid brown small square down
p = "\u001b[38;5;223m█"  #peach
dr = "\u001b[38;5;124m▄"  #red small square down
upr = "\u001b[38;5;124m▀"  #red small square up

# Environment variables
wall = w
floor = upw
roof = dw
tab = "         "

# Lists responsible for drawing the "DONKEY" logo
D = [("  " + r + r + r + r + r + r + r + r + dr + dr),
     (r + r + y + y + y + y + y + y + y + y + y + y + r),
     (r + r + y + y + y + y + y + y + y + y + y + y + y + r),
     (" " + r + r + y + y + y + r + r + r + r + y + y + y + y + r),
     (" " + r + r + y + y + y + y + r + " " + r + y + y + y + y + r),
     (" " + r + r + y + y + y + y + r + " " + r + y + y + y + y + r),
     ("  " + r + r + y + y + y + r + r + y + y + y + y + r),
     ("  " + r + r + y + y + y + y + y + y + y + y + y + r),
     ("   " + r + r + y + y + y + y + y + y + y + r),
     ("   " + r + r + r + r + r + r + r + r + r + upr)]
O = [(dr + "  " + dr + r + r + r + r + r + r + r + r + r + r),
     (r + r + y + y + y + y + y + y + y + y + y + y + r),
     (y + y + y + y + r + r + r + y + y + y + y + y + r),
     (y + y + y + r + " " + r + y + y + y + y + y + r),
     (r + upr + upr + "   " + upr + upr + r + y + y + r),
     (r + r + dr + "   " + dr + r + y + y + y + r),
     (y + r + upr + " " + dr + dr + dr + " " + upr + r + y + y + r),
     (y + r + dr + r + y + y + y + r + dr + r + y + y + r),
     (r + r + y + y + y + y + y + y + y + y + y + y + r),
     ("  " + upr + r + r + r + r + r + r + r + r + r + upr)]
N = [(dr + dr + dr + dr + dr + " " + dr + dr + r + r + r),
     (y + y + y + y + r + r + y + y + y + y + r),
     (y + y + y + y + r + y + y + y + y + r),
     (y + y + y + y + y + y + y + y + y + r),
     (y + y + y + y + y + y + y + y + y + r),
     (y + y + y + y + y + y + y + y + y + r),
     (y + y + y + r + y + y + y + y + y + r),
     (y + y + y + r + r + y + y + y + y + r),
     (y + y + y + y + r + r + r + y + y + y + r),
     (r + r + r + r + r + upr + "  " + upr + r + r)]
K = [(r + r + dr + dr + "   " + dr + dr + dr + dr + dr),
     (y + y + y + r + r + r + r + y + y + y + y + r),
     (y + y + y + y + r + r + y + y + y + y + r),
     (y + y + y + y + r + y + y + y + y + r),
     (y + y + y + y + y + y + y + y + r), (y + y + y + y + y + y + y + r),
     (y + y + y + r + y + y + y + y + r),
     (y + y + y + r + r + y + y + y + y + r + r),
     (y + y + y + r + r + r + y + y + y + y + r),
     (r + r + upr + "  " + upr + r + r + r + r + r)]
E = [(dr + dr + dr + r + r + r + r), (y + y + y + y + y + y + r),
     (y + y + y + y + y + y + y + r), (y + y + r + r + r + r + r + r + r),
     (r + y + y + y + y + y + y + r), (r + r + y + y + y + y + y + y + r),
     (r + y + y + y + y + r + r + r + r + r), (y + y + y + y + y + y + y + r),
     (y + y + y + y + y + y + y + r), (r + r + r + r + r + r + r + r)]
Y = [(dr + dr + dr + "   " + dr + dr + dr + dr + dr + dr),
     (y + y + r + dr + " " + dr + r + y + y + y + y + r),
     (y + y + y + r + dr + r + y + y + y + y + r + upr),
     (y + y + y + y + r + y + y + y + y + r + upr),
     (r + r + r + y + y + y + y + y + y + y + r + upr),
     (r + r + r + r + y + y + y + y + y + r + upr),
     (r + r + y + y + y + y + y + r), (r + r + y + y + y + y + y + r),
     (r + r + y + y + y + y + y + r), (r + r + r + r + r + upr + upr + upr)]

# Lists responsible for drawing the "KONG" logo
K2 = [("    " + r + r + r + r + r + dr + "  " + dr + r + r + r + r + r),
      ("    " + r + y + y + y + y + r + " " + dr + r + y + y + y + y + r),
      ("    " + r + y + y + y + y + r + dr + r + y + y + y + y + r),
      ("     " + r + y + y + y + y + r + r + y + y + y + y + r),
      ("      " + r + y + y + y + y + y + y + y + y + y + r),
      ("       " + r + y + y + y + y + y + y + y + y + r),
      ("        " + r + y + y + y + y + r + y + y + y + y + r),
      ("        " + r + y + y + y + y + r + r + y + y + y + y + r),
      ("        " + r + y + y + y + y + r + upr + r + y + y + y + y + r),
      ("        " + r + r + r + r + r + upr + " " + upr + r + r + r + r + upr)]
O2 = [(dr + dr + dr + dr + dr + dr + dr + dr + dr + dr),
      (y + y + y + y + y + y + y + y + y + y + r),
      (y + y + y + y + r + r + r + y + y + y + y + y + r),
      (y + y + y + y + r + upr + " " + upr + r + y + y + y + y + y + y + r),
      (y + y + r + upr + upr + "     " + upr + upr + r + y + y + y + r),
      (y + y + y + r + r + dr + "     " + dr + r + r + y + y + y + r),
      (y + y + r + upr + "  " + dr + dr + dr + "  " + upr + r + y + y + r),
      (y + r + dr + dr + r + r + y + r + r + dr + dr + r + y + r),
      (y + y + y + y + y + y + y + y + y + y + y + r),
      (r + r + r + r + r + r + r + r + r + upr + upr + upr)]
N2 = [(" " + r + r + r + r + r + r + r + dr + dr + dr + dr + dr),
      (y + y + y + y + r + r + y + y + y + y + y + r),
      (y + y + y + y + r + y + y + y + y + y + r),
      (y + y + y + y + y + y + y + y + r), (y + y + y + y + y + y + y + y + r),
      (y + y + y + y + y + y + y + y + r),
      (y + y + y + r + y + y + y + y + y + r),
      (y + y + y + y + r + r + y + y + y + y + r),
      (r + y + y + y + y + r + r + r + y + y + y + r),
      (r + r + r + upr + upr + upr + upr + r + r + r + r + r + r)]
G = [
    ("   " + dr + r + r + r + r + r + r + r + r + r + r + r + dr + "  "),
    (" " + dr + r + r + y + y + y + y + y + y + y + y + y + y + y + r + "  "),
    (dr + r + y + y + y + y + y + y + y + y + y + y + y + y + y + y + r + " "),
    (r + y + y + y + y + y + r + r + r + r + r + r + r + r + r + r + r) + " ",
    (r + y + y + y + y + y + r + r + r + r + r + r + r + r + r + r + r + r),
    (r + y + y + y + y + y + r + r + r + r + y + y + y + y + y + y + y + r),
    (r + y + y + y + y + y + r + r + r + r + r + r + y + y + y + y + y + r),
    (r + r + y + y + y + y + y + y + y + y + y + y + y + y + y + y + r + upr),
    (r + r + r + r + y + y + y + y + y + y + y + y + y + y + y + r + upr +
     " "),
    ("  " + upr + upr + upr + upr + upr + upr + r + r + r + r + r + r + upr +
     "  ")
]

# List responsible for drawing the "HIGH SCORES" subtitle
HIGH_SCORES = [(w + "  " + w + " " + w + " " + dw + upw + upw + upw + " " + w + "  " + w +
     "   " + w + upw + upw + " " + w + upw + upw + " " + w + upw + w + " " +
     dw + upw + w + "  " + dw + upw + dw + " " + w + upw + upw),
    (w + upw + upw + w + " " + w + " " + w + " " + dw + dw + " " + w + upw +
     upw + w + "   " + w + dw + dw + " " + w + "   " + w + " " + w + " " + w +
     dw + w + "  " + w + dw + w + " " + w + dw + dw),
    (w + "  " + w + " " + w + " " + upw + dw + dw + w + " " + w + "  " + w +
     "   " + dw + dw + w + " " + w + dw + dw + " " + w + dw + w + " " + w +
     " " + upw + w + " " + upw + dw + dw + " " + dw + dw + w)]

# Lists responsible for drawing the "PRESS X" TEXT

PRESS_X = [(r + upr + r + " " + dr + upr + r + "  " + dr + upr + dr + " " + r + upr + upr + " " + r + upr + upr + "    " + upr +dr + " " + dr + upr),
        (r + upr + upr + " " + r +
          dr + r + "  " + r + dr + r + " " + r + dr + dr + " " + r + dr + dr + "      " + r + "  "),
        (r + "   " +  r + " "+ upr + r + " " + upr + dr + dr + " " + dr + dr + r + " " + dr + dr + r + "    " + dr + upr + " "+ upr + dr) ]


def high_scores():

  def file():
    path = "C:/Users/Aluno/Desktop/Donkey-Kong/points.txt"
    scores = (open(path, "r"))
    rows = [int(row.strip()) for row in scores.readlines()]  
    rows.sort(reverse=True)  
    for n in range(len(rows)):
              print(wall + " " * 67 + str(n+1) +". " + str(rows[n]) + " " * (78 - len(str(rows[n]))) + wall + "\n", end='')
    return (len(rows))
  

  for i in range(53):
    if (i == 0):
      print(roof * 150)  #ROOF
    elif (i == 2):
      for n in range(10):
        print(wall + " " * 9 + (D[n] + O[n] + N[n] + K[n] + E[n] + Y[n] +
                                K2[n] + O2[n] + N2[n] + G[n]) +
              "            " + wall + "\n",
              end='')
      i = 12  #DONKEY KONG TITLE
    elif (i == 12 or i == 14 or (i >= 18 and i <= 20) or i==47 or (i>=49 and i<=51)):
      print(wall + " " * 148 + wall + "\n", end='')
    elif (i == 15):
      for n in range(3):
        print(wall + " " * 53 + HIGH_SCORES[n] + " " * 52 + wall + "\n",
              end='')
      i == 18
    elif (i == 21):
      len_scores =file()
      i += len_scores
    elif (i>21 and i<= 45):
      print(wall + " " * 148 + wall + "\n", end='')
    elif (i==46):
      for n in range(3):
        print(wall + " " *58 + PRESS_X[n] + " "*61 + w + "\n", end = '')
      i == 49
    elif (i==52):
      print(floor * 150)
    if WConio2.kbhit():
        (tecla, symbol) = WConio2.getch()
    symbol = ""
    if symbol== "x" or symbol =="X":
      return(1)


teste = high_scores()