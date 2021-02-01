# -*- coding: utf-8 -*-
"""

@author: User
"""

#bisection method to guess the secret number
print('Please think of a number between 0 and 100!')
epsilon=1
x=100
low=0
high=x
ans=int((high+low)/2)
while ans<101:
    print('Is your secret number'+ str(ans)+'?')
    st=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if st=="h":
        high=ans
    elif st=="l":
        low=ans
    elif st=="c":
        print("Game over. Your secret number was: "+str(ans))
        break
    else: 
        print("Sorry, I did not understand your input")
    ans=int((high+low)/2)

    

        
        
    