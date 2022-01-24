import random

rock = ''' 
     __________
----'  ________)
     (__________)
    (___________)
    (__________)
-----'__(_____)

'''
paper = '''

     ______
----'______)_____
        __________)
        ___________)
       __________)
-----'_________)


'''
sciccer = '''

     _______
----'  _____)___________
               _________)
              _________)
        (_______)
-----'__(_____)


 '''


game_images = [rock,paper,sciccer]

user_choice = int(input("what do you want ? type 0 for rock, 1 for paper,2 for scissor\n"))
if user_choice >= 3 or user_choice < 0:
    print("ypu typed an invail number ,you lost!")
else:
       
   print(game_images[user_choice])

   computer_choice = random.randint(0,2)
   print(f"computer choce{computer_choice}")
   print(game_images[computer_choice])
       
   if user_choice == 0 and computer_choice == 2:
      print("you wins!")
   elif computer_choice == 0 and user_choice == 2:
      print("you lose!")
   elif computer_choice > user_choice:
      print("you lose!")
   elif user_choice > user_choice:
      print("you win!")
   elif computer_choice == user_choice:
      print("it's a draw")
      



