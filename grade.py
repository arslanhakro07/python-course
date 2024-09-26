sub1=int(input("please enter your marks:"))
sub2=int(input("please enter your marks:"))
sub3=int(input("please enter your marks:"))

totalmarks=sub1+sub2+sub3
percentage=totalmarks*100/300




if(percentage>=70):
     print(percentage) 
     
elif(percentage>=60):
     print(percentage) 
     print("Grade B")

     print("Grade A")

elif(percentage>=50):
     print(percentage) 
     print("Grade C")


elif(percentage>=40):
     print(percentage) 
     print("Grade D")
    
    
else:
     print(percentage)
     print("you are F")

