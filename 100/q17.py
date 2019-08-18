'''
编写一个程序，计算存款数, D表示存款，W表示取款
'''




# while  True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = float(values[1])
#     if operation == "D":
#         account =+amount
#     elif operation == "W":
#         account =- amount
#
#     else:
#         print("操作错误")
#
# print(account)

netAmount = 0
while True:
    s = input()
    if not s:
        break
    try:
        values = s.split(" ")
        operation = values[0]
        amount = float(values[1])
        if operation == "D":
            netAmount +=amount
        elif operation == "W":
            netAmount-=amount
        else:
            print("操作不合法")
    except:
        print("输入格式有误，请重新输入")
print (netAmount)


'''
学习点:  一点要注意，可以多次回车输入，用到了While True;
        python 只有+= -= 操作符，没有=+的操作符  
        思路：将输入的str类型分开，并进行
'''