#Calculator
while(True):
 print("Calculator".center(44,"*"))  
 c=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice:"))
 if(c in range(1,5)):
  f=int(input("Enter first number:"))
  s=int(input("Enter second number:"))
 if(c==1):
    result=f+s
    print(result)
 elif(c==2):
    result=f-s
    print(result)
 elif(c==3):
  result=f*s
  print(result)
 elif(c==4):
  if(s==0):
      print("0 is not allowed")
  else:
      result=f/s
      print(result)    
 choice=input("To continue the operation press y:")
 if(choice!='y'):
     break
     