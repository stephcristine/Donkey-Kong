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
upp = "\u001b[38;5;223m▀"  #peach
dp = "\u001b[38;5;223m▄"  #peach
dr = "\u001b[38;5;124m▄"  #red small square down
upr = "\u001b[38;5;124m▀"  #red small square up
pink = "\u001b[38;5;198m█" 
uppink = "\u001b[38;5;198m▀"
dpink = "\u001b[38;5;198m▄"


PRINCESS = [("   " + dy + y + y + y + dy),
            (" " + dy + y + p + upp + p  + upp + p + y + dy),
            (" " + y + y+ p + p + p + p + p + y +y ),
            (" " + y + y + dpink + dp + p + p + dpink + y + y),
            ( "  "+ upy+ p + pink + pink + pink + p + upy), 
            ("  " + dpink+pink +  pink + pink + pink + pink + pink +dpink)]
HEART = [(dr + "   " + dr),
        (r + r + dr + r + r), 
         (" " +upr + r + upr)]


POINTS = [(r + upr + upr + dr),
          (r + dr + dr + r),
          (r + "   ")]

for i in range(3):
    print(POINTS[i])