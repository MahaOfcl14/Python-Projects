import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choice = int(input("What do you Choose? Type 0 for rock, 1 for paper or 3 for scissors \n"))
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
#fstring
print("Computer Chose")
print(game_images[computer_choice])

if (user_choice >= 3 or user_choice < 0):
    print("You typed an invalid Number. You Lose!!")
elif(user_choice == 0 and computer_choice == 2):
    print("You Win!!")
elif(computer_choice == 0 and user_choice == 2):
    print("You Lose!!")
elif (computer_choice > user_choice):
    print("You Lose")
elif (user_choice > computer_choice):
    print("You Win!")
elif (computer_choice == user_choice):
    print("It's a Draw!")

