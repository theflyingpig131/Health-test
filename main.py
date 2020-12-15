import Intro
import Game

print("Made by oskar and ELLIOTT")
print("We are making a game for our psa")
print()
print("1 = intro/instructions")
print("2 = Play!")
starting = input(": ")
if starting == "1":
  Intro.main()
if starting == "2":
  Game.main()