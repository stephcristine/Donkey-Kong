import os
import cursor
import WConio2 as WConio2


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
arrow_position = 47

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



#lists responsible for drawing the other objects of the screen

MARIO = [("           " + r + r + r + r + r + r + r + r + r + "            "),
    ("         " + r + r + r + r + r + r + r + r + r + r + r + r + r + r + r + r + "       "),
    ("         " + br + br + br + br + br + br + br + br + lbr + lbr + lbr +lbr + "           "),
    ("       " + br + br + lbr + lbr+ lbr + lbr + br + br + lbr + lbr + lbr +lbr + "  " + lbr + lbr + lbr + lbr + lbr + lbr + "     "),
    ("       " + br + br + lbr + lbr+ lbr + lbr + br + br + br + br + lbr +lbr + lbr + br + br + lbr + lbr + lbr + lbr + lbr + lbr + lbr + "   "),
    ("     " + br + br + br + br + br + br+ lbr + lbr + lbr + lbr + lbr + lbr + lbr +lbr + br + br + br + br + br + br + br + br + "     "),
    ("           "+ lbr + lbr + lbr + lbr + lbr + lbr + lbr +lbr + lbr + lbr + lbr + lbr + lbr + lbr + "       "),
    ("     " + r + r + r + r + r + r + r + r + b + b + b + b + r + r + r + r + "       " + w +w +w + w),
    (w + w + w + w + w + r + r + r + r + r + r + r + r + b + b + b + b + b + b + r + r + r + r + r + r + w + w + w + w + w + w + w ),
    (w + w + w + w + w + w + w + "  " + r + r + r + r + b + b + b + y + y + b + b + b + r + r + r + r + r + r + w + w + w + w + w ),
    (w +w +w + w+"     " + b + b + b + b + b + b + b + b + b + b + b + b + "      " + br+ br + br+ "  "),
    ("       " + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + br + br + br + br + br+ "  "),
    ("     " + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b + b +  b + b + b + b + br + br + br + br + br+ "  "),
    ("   " + br + br + br + br + br + br + b + b + b + b + b + "      " + b + b +  b + b + b + br + br + br + br + br + "  "),
    ("   " + br + br + br + br + br + br + "                       "),
    ("     " + br + br + br + br + br + br + "                     "),]


simbolo=''  

# Function that actually draws the home screen
def last_screen():
  for i in range(53):
    if (i == 0):
      print(roof * 150)
    elif (i== 1 or i==13 or (i >=14 and i<=26) or (i >=44 and i<=49) or (i>=50 and i<=51)):
      print(wall + " " * 148 + wall + "\n", end='')
    elif (i == 2):
      for n in range(10):
        print(wall + "         " + (D[n] + O[n] + N[n] + K[n] + E[n] + Y[n] +
                                    K2[n] + O2[n] + N2[n] + G[n]) +
              "            " + wall + "\n",
              end='')  # #DONKEY KONG TITLE
      i = 12

    elif (i == 27):
        for i in range(16):
            print(wall + " " * 58 + MARIO[i] + " " * 58 + wall + "\n", end='')
        i==43

    elif (i == 52):
      print(floor * 150)

    simbolo=''  

    if WConio2.kbhit():
        (tecla, simbolo) = WConio2.getch()
    if simbolo == 'x' or simbolo == 'X':
        return(1)
(last_screen)