# This is a simple enchanting game.

import random

while True:
  EnchTry = 5
  Ench = 0
  EnchLuck = 31
  EnchTryEnd = 0
  TimeAmuLuck = random.randint(1, 100)


  print ('Hello, stranger. Im White Mage, Siphon. Please, tell me your name')  # Greets
  SName = input()
  if SName == str(''):
    SName = 'Anonymus'
    print ('Oh... If you dont mind, i will call you Anonymus. ')
  else:
    print ('Nice to meet you, '+ SName + '!')               # Greets



  print (SName + ' !!! I will give you a present. Simple Sword and 5 tries to enchant it. Would you like to try enchant it? (y)es or (n)o ?')  # Q1
  Q1 = input()
  while Q1 == str ('y') or str ('n'):  # Will do if you want play a game (Q1)
    if Q1 == str ('y'):
        print ('Lets start and Good Luck')      
        while EnchTry != 0 and EnchLuck > 30:  # Will repeat if you Lucky.           
            print ('You have ' + str (EnchTry) + ' tries! But be careful! Enchanting can break your sword! Now you have Sword+ ' + str (Ench) + ' . Do you want to enchant it? (y)es or (n)o ?') # If you want continios Q2
            Q2 = input()
            while Q2 == str ('y') or str ('n'):
                if Q2 == str ('y'):        # Will do if you want (Q2)
                    EnchTry = EnchTry - 1
                    EnchTryEnd = EnchTryEnd + 1
                    EnchLuck = random.randint(1, 100)
                    Ench = Ench + 1
                    break
                elif Q2 == str ('n'):    # Will stop if you dont want (Q2)
                    print (' Okay. If you wish ...')
                    EnchTry = 0
                    break
                else:
                    print ('Please, type y or n.')
                    Q2 = input()
        break
    elif Q1 == str ('n'):      # Will do if you dont want to play (Q1)
        print ('Okay. Just take my present, please.')
        break
    else:
        print ('Please, type y or n.')
        Q1 = input()
  if EnchLuck <= 30:      # Bad Luck you broke your sword
    print ('Oops! you have broken your sword. Very sad. Take this stick and be careful in your adventure!')
  elif EnchLuck > 30 and Ench != 0 :     # Show you a score
    print ('You spent ' + str (EnchTryEnd) + ' tries. Take your Sword+ ' + str (Ench) + '  and good luck in your adventure')
  elif EnchLuck > 30 and Ench == 0 :     # No Risk
    print ('You decided to keep your Sword without enchant. Please take it and take care!')
  else:                  # will Thanks you if you decided to not play (Q1)
    print ('Thank you! Bye, ' + SName)
  while True:
    print('Do you want to use TimeTravel amulet? (y)es or (n)o : ')     # Q3
    Q3 = input()
    if Q3 in ('y', 'n'):                   # checking answer (Q3)
       break
    print ('TimeTravel amulet couldnt understand your wish, ' + SName + ' Please, type y or n.') # Ask type y or n
  if Q3 == 'y' and TimeAmuLuck > 11:      # repeat Adventure
    print ('TimeTravel amulet sent you to the past ...')
    continue
  elif TimeAmuLuck <= 10:
    print ('TimeTravel amulet exploded and sent you to the VOID... which you couldnt escape ...')
    print ('VOID      NO ESCAPE    ' * 100)      # Very bad ending
    break
  else:
    print ('Goodbye, ' + SName)  # stop Adventure
    break

  

