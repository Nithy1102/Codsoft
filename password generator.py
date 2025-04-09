#Password generator 
import random
while(True):
 print("Password Generator".center(44,"*"))
 password=""
 t='''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''  
 n=int(input("Enter the length of password:"))
 for i in range(0,n):
     password+=random.choice(t)
 print(password)    
 choice=input("To continue the operation press y:")
 if(choice!='y'):
     break
     