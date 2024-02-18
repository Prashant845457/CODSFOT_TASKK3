def calculator():
    while(1):
        a = int(input("Enter the first value: "))
        oper = input("Enter the operator: ")
        b = int(input("Enter the second value: "))
        if oper == '+':
            print(f"The answer is: {a + b}")
        if oper == '-':
            print(f"The answer is: {a - b}")
        if oper == '*':
            print(f"The answer is: {a * b}")
        if oper == '/':
            if b == 0:
                print("Error: zero is not divisible!")
            else:
                print(f"The answer is: {a / b}")
        if oper == '%':
            if b == 0:
                print("Error: modulo operation can't do with zero!")
            else:
                print(f"The answer is: {a % b}")
        if oper != '+' and oper != '-' and oper != '*' and oper != '/' and oper != '%' :
            print("Error: Invalid operator! Try Again!")
            break
        more = int(input("If you want to do more operations press '1' othrwise '0' for exit : "))
        if more == 1 or more == 0:
            if more == 1:
                continue
            else:
                break
        else:
            more = int(input("Invalid option. Please enter '0' or '1': "))
            if more == 1:
                continue
            else:
                break
calculator()
