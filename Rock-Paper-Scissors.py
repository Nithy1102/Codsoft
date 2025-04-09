import random 
print("ROCK PAPER SCISSORS".center(44,"*"))
l=["ROCK","PAPER","SCISSORS"]
while True:
    for i in range(0,3):
        print(i+1,".",l[i])
    c=int(input("Enter your choice:"))
    pc=l[c-1]    
    cc=random.choice(l)
    print("Your choice:",pc)
    print("Computer's choice:",cc)
    if(pc==l[1] and cc==l[0] or pc==l[0] and cc==l[2] or pc==l[2] and cc==l[1]):
        print("Player wins")
    elif(pc==cc):
        print("It's a tie")
    else:
        print("Computer wins")
    choice=input("For another round press y:")
    if(choice!='y'):
        break            
        
     
        
        
            
    
    