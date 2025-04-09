#TO-DO List
list=[]
n=int(input("Enter the number of tasks to be added:"))
for i in range(0,n):
    task=input("Enter your task:")
    list.append(task)
while(True):
 c=input("To show the tasklist press s\nTo update the task press y\nTo add the task press a:")
 if(c=='y'):
    task_number=int(input("Enter your task number:"))
    t=input("Enter your updated task:")
    list[task_number-1]=t
 elif(c=='a'):
    t=input("Enter your new task:")
    list.append(t)
 elif(c=='s'):
  print("Your To-Do list".center(44,"*"))
  for i in range(0,len(list)):
    print(i+1,".",list[i])
 choice=input("To continue the operation press y:")
 if(choice!='y'):
     break
     