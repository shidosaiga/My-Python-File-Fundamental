print("enter your score to calculate for you grade")
math = int(input("input you Math score: "))
science = int(input("input you Science score: "))
computer = int(input("input you Computer score: "))
Eng = int(input("input you English score: "))
text = "Grade"

sum = math+science+computer+Eng
avg = sum/4
print (f"your score total is :{avg}")


if avg >= 95 and avg <=100:
    print(f"{text} : A+")
elif avg >=90 and avg <= 94.9:
    print(f"{text} : A")
elif avg >=85 and avg <= 89.9:
    print(f"{text} : B+")
elif avg >=70 and avg <= 84.9:
    print(f"{text} : B")
elif avg >=60 and avg <= 69.9:
    print(f"{text} : C")
elif avg >=50 and avg <= 59.9:
    print(f"{text} : D")
elif avg <= 49:
    print(f"{text} : F")       
else:
    print(f"{text} : ERROR SCORE MAXIMUM")
    
        
        
        
        
    