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
        if char == "/" or char == "*" or char == "+" or char == "-" :
            lst.append(emp_str)
            lst.append(char)
            emp_str = ""
        else:
            emp_str = emp_str + char
    lst.append(emp_str)
    return lst

def update_lst(i, lst):
    num1 = float(lst[i-1])
    op = lst[i]
    num2 = float(lst[i+1])
    
    result = calc_main(num1, op, num2)
    del lst[i-1:i+2]
    lst.insert(i-1,result)
    return lst

def dmas(lst):
    for i in range(len(lst)):
        if lst[i] == "/":
            lst = update_lst(i, lst)
            # print(lst)
            dmas(lst)
            break
    for i in range(len(lst)):
        if lst[i] == "*":
            lst = update_lst(i, lst)
            dmas(lst)
            break
    for i in range(len(lst)):
        if lst[i] == "+":
            lst = update_lst(i, lst)
            dmas(lst)
            break
    for i in range(len(lst)):
        if lst[i] == "-":
            lst = update_lst(i, lst)
            dmas(lst)
            break
    return lst


def main():
    # input_str = "1.5 + 2 * 3 / 4 - 5"
    # input_str = "3.5 + 2"
    input_str = input()
    lst = str_cleanup(input_str)
    return print(dmas(lst)[0])


if __name__ == "__main__":
    main()
