# The script of the game goes in this file.

# Define main protagonist

define main = Character('Hiroshi', color="#ffffff")
define k = Character('Kasuka', color="#ffffff")
define m = Character('Mika', color="#ffffff")
define r = Character('Rin', color="#ffffff")

# Define side characters
define d = Character('Daichi', color="#ffffff")
define t = Character('Tomo', color="#ffffff")

# Define affection points
default kasuka_affection = 0

# Define flag
default flag_walk_home = False
default flag_encourage_draw = False
default flag_forest = False
default flag_confession = False
default flag_love_jam_partner = False

# The game starts here.

label start:
    jump chapter0

    
