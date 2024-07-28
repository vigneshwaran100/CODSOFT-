import random

def RPS(u_input):
    u_input.lower()
    component=["rock","paper","scissors"]
    computer_input=random.choice(component)
    print("this is you and computer inputs:",u_input,computer_input)
    if u_input==computer_input:
        print("It is tie")
        pass
    elif u_input=='paper' and computer_input=='rock':
        print("You Win")    
    elif u_input=='scissor' and computer_input=='paper':
        print("You Win")
    elif u_input=='rock' and computer_input=='scissor':
        print("You Win")
    else:
        print("Computer Win")
   
    

u_input=input("enter rock paper scissor: ")
RPS(u_input)