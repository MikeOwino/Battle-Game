#!/bin/python3
import random, time
from termcolor import colored, cprint
from player import *
from special import *
from helper import *

cprint("Welcome to the battle game.", 'green')
print("")
time.sleep(0.1)
cprint("Do you want to be the hero or the villain? (Type 'h' for hero and 'v' for villain.)", 'yellow')
mode = input(">")

if mode != 'h' and mode != 'v':
  while True:
    print("Invalid input.")
    mode = input(">")
    print("")
    
    if mode == 'h' or mode == 'v':
      break

heroes = ['Spiderman', 'Pikachu', 'Hercules', 'Jedi']
villains = ['Voldemort', 'Thanos', 'Medusa']
if mode == 'h':
  cprint("The computer will be the villain, and you will be the hero.", 'yellow')
  userchars = heroes
  botchars = villains
else:
  cprint("The computer will be the hero, and you will be the villain.", 'yellow')
  userchars = villains
  botchars = heroes

print("")
time.sleep(0.2)
cprint("Do you want to choose your character or do you want it to be random? (Type 'c' for choose and 'r' for random.)", 'yellow')
answer = input(">")
print("")


  
if answer != 'c' and answer != 'r':
  while True:
    print("Invalid input.")
    answer = input(">")
    print("")
    
    if answer == 'c' or answer == 'r':
      break

if answer == 'c':
  cprint("Choose one of the following characters to fight against the enemy!", 'yellow')
  print("")
  
  time.sleep(0.2)
  for i in userchars:
    print(i)
  player = input(">")
  print("")
    
  if player not in userchars:
    while True:
      cprint("Please enter one of the characters mentioned above.", 'yellow')
      player = input(">")
      print("")
      
      if player in userchars:
        break

elif answer == 'r':
  player = random.choice(userchars)
  cprint("Your character is...", 'yellow')
  time.sleep(0.2)
  cprint(player + "!", 'magenta')
  print("")
  time.sleep(0.2)
  

villain = random.choice(botchars)

if player == "Spiderman":
  user = Spiderman()
      
elif player == "Pikachu":
  user = Pikachu()
    
elif player == "Hercules":
  user = Hercules()
    
elif player == "Jedi":
  user = Jedi()

elif player == "Voldemort":
  user = Voldemort()

elif player == 'Thanos':
  user = Thanos()

elif player == "Medusa":
  user = Medusa()

if villain == "Spiderman":
  bot = Spiderman()
      
elif villain == "Pikachu":
  bot = Pikachu()
    
elif villain == "Hercules":
  bot = Hercules()
    
elif villain == "Jedi":
  bot = Jedi()

if villain == 'Voldemort':
  bot = Voldemort()

elif villain == 'Thanos':
  bot = Thanos()
  
elif villain == "Medusa":
  bot = Medusa()
  

cprint("The enemy {} will be fighting against is...".format(player), 'cyan')
time.sleep(0.2)
cprint("{}!".format(villain),'blue')

time.sleep(0.2)
get_status(user, bot)
time.sleep(0.2)

while True:
  user_move(user, bot)
  time.sleep(0.2)
  
  if user.health <= 0:
    cprint("{} has no more health...".format(player), 'red')
    time.sleep(0.2)
    print("Computer wins!")
    break

  elif bot.health <= 0:
    cprint("{} has no more health...".format(villain), 'red')
    time.sleep(0.2)
    print("You win!")
    break
  
  bot_move(user, bot)
  time.sleep(0.2)
  
  if user.health <= 0:
    cprint("{} has no more health...".format(player), 'red')
    time.sleep(0.2)
    print("Computer wins!")
    break

  elif bot.health <= 0:
    cprint("{} has no more health...".format(villain), 'red')
    time.sleep(0.2)
    print("You win!")
    break
  
      
      
    