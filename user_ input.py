'''a = input("enter yoyr name : ")
b = int(input("enter yopur age : "))
print(type(a),type(b))

a= 1.2
print(type(int(a)))
print(int(a))

c=2+3j
print(type(c))

ab = 11
print(float(ab))


# Accept a string value from the user
user_input = input("Enter a string: ")

# Display the string entered by the user
print("You entered:", user_input)


def calculate_average_marks(sub1,sub2,sub3):
    total_marks = sub1+sub2+sub3
    average_marks = total_marks/3
    return average_marks
a = int(input("enter your marks in sub1 : "))
b = int(input("enter your marks in sub2 : "))
c = int(input("enter your marks in sub3 : "))

average_marks = calculate_average_marks(a,b,c)
print(average_marks)

a = float(input("enter your marks in sub1 : "))
b = float(input("enter your marks in sub2 : "))
c = float(input("enter your matks in sub3 : "))

total_marks = a+b+c
average_marks = total_marks/3

print("Average marks: ", average_marks)

per = int(input("Enter Percentage : "))
print(per)
if per>=90:
    print("A+ Grade")
elif per<90 and per>=60:
    print("A grade")
elif per<60 and per>=50:
    print("B grade")
elif per<50 and per>=35:
    print("C grade")
else:
    print("F")'''

richter_magnitude = float(input(" Enter magnitude = "))

if richter_magnitude > 10:
    print("good")
elif richter_magnitude < 6.5:
    print("bad")
else:
    print("average")
