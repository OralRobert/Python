a = input("enter yoyr name : ")
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



