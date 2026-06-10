# Grade ky liya
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))
print("Your Grade:", get_grade(marks))
# calculator ky liya 
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# User input
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))
operation = input("Enter operator (+, -, *, /): ")

# Result
result = calculator(num1, num2, operation)
print("Result:", result)
# for Table 
def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

n = int(input("Enter num for table : "))
table(n)