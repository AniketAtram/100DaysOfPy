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

rps_choices = [rock, paper, scissors]

# 0 -> rock 1->paper 2->scissors
user_selection = int(input("What do you choose? 0 for rock 1 for paper 2 for scissors: "))
comp_selection = random.randint(0,2)
print("You've chosen:")
print(rps_choices[user_selection])
print("Computer chose:")
print(rps_choices[comp_selection])
if user_selection == 0 and comp_selection == 2:
    print("Rock wins against scissors!")
    print("You've won!")
elif comp_selection == 0 and user_selection == 2:
    print("Rock wins against scissors!")
    print("Computer won!")
elif user_selection == 1 and comp_selection == 0:
    print("Paper wins against rock!")
    print("You've won!")
elif comp_selection == 1 and user_selection == 0:
    print("Paper wins against rock!")
    print("Computer won!")
elif user_selection == 2 and comp_selection == 1:
    print("Scissors wins against paper!")
    print("You've won!")
elif comp_selection == 2  and user_selection == 1:
    print("Scissors wins against paper!")
    print("Computer won!")
else:
    print("It's a draw!")
