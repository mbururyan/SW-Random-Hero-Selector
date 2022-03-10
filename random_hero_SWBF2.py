# Random number for picking heroes in Battlefront
import random

# Chose faction between Hero or Villain

faction = input('You want a Hero or a Villain? : ')
print(faction)

# If statement

if faction == 'Hero':
    heroes = ['luke', 'leia', 'han', 'chewbacca', 'lando', 'rey', 'anakin', 'obiwan', 'yoda', 'finn']
    print('\nYour hero this round will be ... : ', random.choice(heroes))

elif faction == 'Villain':
    villains = ['boba', 'bossk', 'vader', 'palpatine', 'kylo', 'maul', 'iden', 'phasma', 'grievous', 'dooku']
    print('\nYour villain this round will be ... : ', random.choice(villains))
else:
    print('Choose your faction again')

# Lightside




# Villains

# 
# 

