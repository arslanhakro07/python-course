sub1=int(input("please enter your marks:"))
sub2=int(input("please enter your marks:"))
sub3=int(input("please enter your marks:"))

totalmarks=sub1+sub2+sub3
percentage=totalmarks*100/300

if(sub1>33) and(sub2>33)and (sub3>33):
     print(percentage) 
     print("you are pass")
    
else:
     print(percentage)
     print("you are fail")
