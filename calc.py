def calc_main(num1,op,num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        return print("Invalid operator")
    return result


def str_cleanup(input_str):
    lst = []
    input_str = input_str.replace(" ", "")
    emp_str = ""

    for char in input_str:
        if char == ".":
            emp_str = lst[-1] + "."
            del lst[-1]
            continue
        lst.append(emp_str + char)
        emp_str = ""
    return lst



def main():
    # input_str = "1 + 2 * 3 / 4 - 5"
    # input_str = "3.5 + 2"
    input_str = input()
    lst = str_cleanup(input_str)
    
    while len(lst) >= 3:
        num1 = float(lst[0])
        op = lst[1]
        num2 = float(lst[2])
        
        result = calc_main(num1, op, num2)
        del lst[0:3]
        lst.insert(0,result)
    
    return print(result)


if __name__ == "__main__":
    main()
