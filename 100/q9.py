'''
将所有输入字符大写输出
可以回车输入
'''


lines = []
while True:
    oring_string = input()
    if oring_string:
        lines.append(oring_string.upper())
    else :
        break



print(' '.join(lines))

'''
学习点：这里最主要的是回车输入， 如果简单的用upper, 不写循环，那么会出现回车输入直接输出内容，这里用一个while 循环和if循环，如果输入为空，直接停止循环。
        学习一下while True 的作用吧
        while True 在这里的作用就是每次输入回车之后回到while判断条件，然后继续输如，如果输入为空，那么直接break循环。 
        总结一下就是要继续执行某个操作，知道这个操作条件执行不下去，break，例如写一个登录程序，当输入用户名密码不正确的时候，你需要重新让他输入，那么，while True就可以让程序回到重新输入
        的地方，继续执行，直到登录成功，break
        
        关于if判断条件：表达式可以是一个单纯的布尔值或变量，也可以是比较表达式或逻辑表达式
        当下面的值作为 bool 表达式时，会被解释器当作 False 处理：
        False、None、0、""、()、[]、{}  
        本例中，if 的判断条件是一个字符串，如果字符串为空，那么判断条件为假，所以跳出循环
'''