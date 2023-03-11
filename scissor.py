import random
option=["Rock" , "Paper" , "Scissor"]
print("ROCK PAPER SCISSOR GAME")
print("--------------------------------------------------------------")
print("PLAYERS TURN")
print("--------------------------------------------------------------")
user_choice=input("WHAT DO U WANT TO CHOOSE ? (Rock , Paper , Scissor)")
print("--------------------------------------------------------------")
print("COMPUTER TURN")
computer_choice =random.choice(option)
print("COMPUTER CHOOSE "+str(computer_choice))
print("--------------------------------------------------------------")
print("RESULT:-")
print("--------------------------------------------------------------")
if (user_choice == "Rock" and computer_choice=="Scissor"):
    print("You win ")   
elif (computer_choice== "Rock" and user_choice== "Scissor"):
    print("You Lose")
    
elif (computer_choice== "Paper" and user_choice== "Rock"):
    print("You Lose")
   
elif (user_choice== "Paper" and computer_choice== "Rock"):
    print("You Win")
   
elif (user_choice== "Scissor" and computer_choice== "Paper") :
    print("You Win")
   
elif (computer_choice== "Scissor" and user_choice== "Paper"):
    print("You Lose")
    
    
elif (user_choice== "Rock" and computer_choice== "Rock"):
    print("Draw")
elif (user_choice=="Paper"and computer_choice=="Paper"):
    print("Draw")
elif (user_choice=="Scissor" and computer_choice=="Scissor"):
    print("Draw")
