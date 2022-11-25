from createhero import *
import os


os.system("cls")
p1 = make_hero(hp_curret= 15,money=100)
show_hero(p1)
play_dice(p1, 15)
play_dice(p1, 100)
show_hero(p1)
