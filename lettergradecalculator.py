text = """
Letter Grade Calculation
"""
print(text)

num1 = int(input("Type your first midterm score: "))
num2 = int(input("Type your second exam score: "))
num3= int(input("Type your final exam score: "))

result = (num1*0.3)+(num2*0.3)+(num3*0.4)
print(result)

if result>=90:
    print("Your letter grade is AA,excellent")
elif result>=85:
    print("Your letter grade is BA,good")
elif result>=80:
    print("Your letter grade is BB,good")
elif result>=75:
    print("Your letter grade is CB,satisfactory") 
elif result>=70:
    print("Your letter grade is CC,satisfactory")  
elif result>=65:
    print("Your letter grade is DC,marginal pass")
elif result>=60:
    print("Your letter grade is DD,marginal pass")
elif result>=50:
    print("Your letter grade is FD,inadequate")
elif result>=0:
    print("Your letter grade is FF,inadequate)
