
result = 0
fNum = int(input("Enter first number: "))

while True:
    to_do = input("Enter operator (+, -, *, /) or 'exit' to quit: ")

    if to_do == "exit":
        break

    sNum = int(input("Enter second number: "))

    if to_do == '+':
        result = fNum + sNum
    elif to_do == '-':
        result = fNum - sNum
    elif to_do == '*':
        result = fNum * sNum
    elif to_do == '/':
        result = fNum / sNum
    else:
        print("Invalid operator")
        continue
    
    fNum = result
    print("Result:", result)

    go = input("If you wanna clear the result type 'cls':")

    if go == "cls":
        fNum = int(input("Enter first number: "))
