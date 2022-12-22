import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

question = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
random_int = random.randint(0,2)
if question == random_int:
    print("DRAW")
if question == 0 and random_int == 1:
        print(f"{paper} you lose! paper wins.")
if question == 0 and random_int == 2:
    print(f"{rock} you win! rock wins.")
if question == 1 and random_int == 0:
    print(f"{paper} you win! paper wins.")
if question == 1 and random_int == 2:
    print(f"{scissors} you lose! scissors wins.")
if question == 2 and random_int == 0:
    print(f"{rock} you lose! rock wins")
if question == 2 and random_int == 1:
    print(f"{scissors} you win! scissors wins.")