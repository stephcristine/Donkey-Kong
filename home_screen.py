import os
import WConio2 as WConio2
import cursor

os.system('cls')
cursor.hide()


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

# Lists responsible for drawing the "KONG DONKEY" subtitle
KONG = [(w + " " + dw + upw + " " + w + upw + w +" " + w + dw +" "+ w + " " + dw + upw + upw + upw), 
        (w + w + "   " + w + " " + w + " " + w + " " + upw + w + " " + w + " " +dw + dw), 
        (w + " " + upw + dw + " " + w + dw + w + " " + w + "  " + w + " "+ upw + dw + dw +  w)] 

DONKEYS = [( w + upw + dw + " " + w + upw + w+" " + w + dw +" "+ w + " "+ w + " "+dw + upw + " " +dw + upw + w + " " + upw + dw + " " + dw + upw + " " + dw + " " +w + upw + upw),
           (w + " " + w + " " + w + " " + w+ " " + w + " " + upw + w + " " + w + w + "   " + w + dw + w + "   " + w + "   " + upw + " " + w + dw + dw), 
           (w + dw + upw + " " + w + dw + w+ " " + w + "  " + w + " " + w + " " + upw + dw + " " +upw + dw + dw + "   " + w + "     " + dw + dw + w)]

VERSION = [(upw + dw + "   " + dw + upw + " " +w + upw + dw + "  "+ w + upw + dw + "  " +w + upw + upw + " "+ w + " " + w + upw + w + " " + w + dw +" " + w), 
           (" "+ upw +dw + " "+ dw+ upw + "  " + w + dw + w + "  " + w + dw + w + "  " + w + dw + dw + " "+ w + " " + w + " "+ w + " " + w + " " + upw + w), 
           ("  "+upw + dw + upw +  "   " +upw + dw + dw + "  " + w + " "+ upw + w+ " " + dw + dw + w + " "+ w + " " + upw + dw + w + " " + w + "  " + w)]

# Lists responsible for drawing other scenery objects
BARREL = [(" " + do + o + lo + o + o + o + o + o + o + lo + o + do + " "),
          (b + b + b + b + b + b + b + b + b + b + b + b + b + b),
          (o + lo + lo + lo + o + o + o + o + o + o + lo + lo + lo + o),
          (o + lo + lo + lo + o + o + o + o + o + o + lo + lo + lo + o),
          (o + lo + lo + lo + o + o + o + o + o + o + lo + lo + lo + o),
          (b + b + b + b + b + b + b + b + b + b + b + b + b + b),
          (" " + upo + o + lo + o + o + o + o + o + o + lo + o + upo + " ")]

OIL = [(upb + b + b + b + b + b + b + b + b + b + b + upb),
       (" " + b + b + b + b + b + b + b + b + b + b + " "),
       (" " + b + w + w + w + b + w + b + w + b + b + " "),
       (" " + b + w + b + w + b + w + b + w + b + b + " "),
       (" " + b + w + w + w + b + w + b + w + w + b + " "),
       (db + b + b + b + b + b + b + b + b + b + b + db)]

MONKEY = [
    ("             " + dbr + br + br + br + br + br + br + br + dbr + "  "),
    ("           " + dbr + br + lbr + lbr + lbr + lbr + br + lbr + lbr + lbr +
     lbr + br + dbr),
    ("         " + dlbr + lbr + br + br + lbr + w + upw + upw + br + upw +
     upw + w + lbr + br + br + lbr + dlbr + "        "),  #33
    ("      " + dbr + br + br + br + lbr + lbr + lbr + lbr + lbr + lbr +
     uplbr + uplbr + uplbr + lbr + lbr + lbr + lbr + lbr + lbr + br + br + br +
     dbr + "     "),  #33
    ("    " + dbr + br + br + br + br + br + lbr + lbr + uplbr + uplbr +
     uplbr + uplbr + uplbr + uplbr + uplbr + uplbr + uplbr + uplbr + uplbr +
     lbr + lbr + br + br + br + br + br + dbr + "   "),  #33
    ("  " + dbr + br + br + br + br + br + br + br + br + lbr + dlbr + lbr +
     lbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr + dlbr + lbr + br + br +
     br + br + br + br + br + br + dbr + " "),  #33
    ("  " + br + br + br + br + mbr + br + br + br + br + br + br + br + br +
     br + br + br + br + br + br + br + br + br + br + br + br + br + mbr +
     br + br + br + br + " "),  #33
    ("  " + br + br + br + br + br + mbr + mbr + br + br + br + br + br + br +
     br + br + br + br + br + br + br + br + br + br + br + mbr + mbr + br +
     br + br + br + br + " "),  #33
    ("  " + br + br + br + br + br + br + mbr + mbr + mbr + br + lbr + lbr +
     lbr + lbr + lbr + br + lbr + lbr + lbr + lbr + lbr + br + mbr + mbr +
     mbr + br + br + br + br + br + br + " "),  #33
    ("    " + upbr + br + br + br + br + br + br + br + lbr + lbr + lbr + lbr +
     lbr + br + lbr + lbr + lbr + lbr + lbr + br + br + br + br + br + br +
     br + upbr + "   "),  #33
    ("     " + br + br + br + br + br + br + br + br + uplbr + uplbr + uplbr +
     uplbr + br + uplbr + uplbr + uplbr + uplbr + br + br + br + br + br + br +
     br + br + "    "),  #33
    ("    " + dbr + br + br + br + br + br + br + br + br + br + br + br + br +
     br + br + br + br + br + br + br + br + br + br + br + br + br + dbr +
     "   "),  #33
    ("   " + dbr + br + br + br + br + br + br + br + br + br + br + br + br +
     br + br + br + br + br + br + br + br + br + br + br + br + br + br + br +
     dbr + "  "),  #33
    ("   " + br + br + br + br + br + br + br + br + br + br + br + br + upbr +
     "    " + upbr + br + br + br + br + br + br + br + br + br + br + br +
     "  "),  #33
    ("   " + br + br + br + br + br + br + br + br + br + br + upbr +
     "        " + upbr + br + br + br + br + br + br + br + br + br +
     "  "),  #33
    (" " + dlbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr + uplbr +
     "            " + uplbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr + lbr +
     dlbr)
]

FIRE = [
    ("  " + dw + "    " + dr + "    "),
    ("  " + dr + "  " + upy + "  " + dy + "  " + dw),
    ("   " + dy + " " + dr + y + dy + " " + y + dr + " "),
    (" " + dr + r + upr + " " + upr + y + y + w + y + r + dr),
    (" " + y + w + dr + dy + r + y + w + dr + r + r + r),
    (" " + upy + w + r + r + w + y + r + w + w + upy + upr),
]

ARROW = [("    " + r + dr + " "), 
         (upr + upr + upr + upr + r + r + upr), 
         ("    "+ upr  + "  ")]

#Lists responsable for drawing the Home Screen Buttons
NEW_GAME = [                                    #
    (w + dw +" " + w + " " +dw + upw + dw + " " + w + "     " + w + "   " + dw + upw + upw + w + " " + dw + upw + dw + " " + w + dw + " " + dw + w + " " +dw + upw + dw),
    (w + " " + upw + w + " " + w + dw + w + " " + upw + dw + " " + dw + " " + dw + upw + "   " + w + " " +dw + dw + " " + w + dw + w + " " + w + " " + upw + " " + w + " " + w + dw + w),
    (w + "  " + w + " " + upw + dw + dw + "  " + upw + dw + upw  + dw + upw + "    " + upw + dw + dw +  w + " " + w + " " + w + " " + w + "   " + w + " " + upw + dw + dw)
]

HIGH_SCORES = [(w + "  " + w + " " + w + " " + dw + upw + upw + upw + " " + w + "  " + w + "   "  + w + upw + upw + " " + w + upw + upw + " " + w + upw + w + " " + dw + upw + w + "  " +dw + upw + dw + " " + w + upw + upw),
               (w + upw + upw + w + " " + w + " " + w + " " +dw + dw + " "+ w + upw + upw +w + "   " + w + dw + dw + " " + w + "   " + w + " "+ w + " " + w + dw + w + "  " + w + dw + w + " "+ w + dw + dw), (w + "  " + w + " " + w + " " + upw + dw + dw +  w +" " +  w + "  " + w + "   " + dw + dw + w + " " + w + dw + dw + " " + w + dw + w + " " + w + " " + upw + w + " " + upw + dw + dw + " " + dw + dw + w)]


#Function that actually draws the home screen
def home_screen(arrow_position):

    for i in range(53):
      if (i == 0):
        print(roof * 150)
      elif (i == 2):
        for n in range(10):
          print(wall + "         " + (D[n] + O[n] + N[n] + K[n] + E[n] + Y[n] +
                                      K2[n] + O2[n] + N2[n] + G[n]) +
                "            " + wall + "\n",
                end='')  # #DONKEY KONG TITLE
        i = 12
      elif (i == 14):
        for n in range(6):
          if n >= 1 and n<=3:
            print(wall + "          " + FIRE[n] + " " * 10 + KONG[n-1] + "   " + DONKEYS[n-1] + " " *38 + FIRE[n] +
                "            " + wall + "\n",
                end='')
          elif n==5:
            print(wall + "          " + FIRE[n] + " " * 55 + VERSION[n-5] +  " " *17 + FIRE[n] +
            "          " + wall + "\n",
            end='')
          else:
            print(wall + "          " + FIRE[n] + " " * 104 + FIRE[n] +
                "          " + wall + "\n",
                end='')  #FIRE
        i = 20
      elif (i == 21):
        for n in range(6):
          if n == 0 or n == 1:
            print(wall + "          " + OIL[n] + " " * 55 + VERSION[n+1] +  " " *17 + OIL[n] +
            "          " + wall + "\n",
            end='')
          elif n>= 1 and n<= 3:
            print(wall + "          " + OIL[n] + " " * 104 + OIL[n] +
                  "          " + wall + "\n",
                  end='')
          else:
            print(wall + "          " + OIL[n] + " " * 38 + MONKEY[n - 4] +
                  " " * 42 + OIL[n] + "          " + wall + "\n",
                  end='')
        i = 26
      elif (i == 26):
        for n in range(7):
          print(wall + "  " + BARREL[n] + BARREL[n] + " " * 30 + MONKEY[n + 2] +
                " " * 24 + BARREL[n] + BARREL[n] + "  " + wall + "\n",
                end='')  #BARRIL
        i = 33
      elif (i == 33):
        for n in range(7):
          print(wall + "  " + BARREL[n] + BARREL[n] + " " * 30 + MONKEY[n + 9] +
                " " * 24 + BARREL[n] + BARREL[n] + "  " + wall + "\n",
                end='')  #BARREL
        i = 40
      elif (i == 40 or i == 44 or i == 45 or i == 47 or i == 50 or i == 51):
        print(wall + " " * 148 + wall + "\n", end='')
      elif (i == 41):
        for n in range(3):
          if arrow_position==42:
            print(wall + " " * 46 + ARROW[n] + " " *6 + NEW_GAME[n] + " " * 52 + wall + "\n", end='')
          else:
            print(wall + " " * 59 + NEW_GAME[n] + " " * 52 + wall + "\n", end='')
          i = 43
      elif (i == 46):
        for n in range(3):
          if arrow_position==47:
            print(wall + " " * 46 + ARROW[n] + " " *3 + HIGH_SCORES[n] + " " * 49 + wall + "\n", end='')
          else:
            print(wall + " " * 56 + HIGH_SCORES[n] + " " * 49 + wall + "\n", end='')
          i = 49
      elif (i == 52):
        print(floor * 150)

      symbol =''

      if WConio2.kbhit():
            (tecla, symbol) = WConio2.getch()
      if symbol == 'w':
        arrow_position -= 5
      elif symbol == 's':
        arrow_position += 5
      elif symbol == ' ':
         if arrow_position == 42:
             return 0
         elif arrow_position == 47:
             return 1




