'''
编写一个函数计算5/0,并用try - except捕获异常
'''

def catchExc():
    try:
        r = 5/0

    except ZeroDivisionError:
        print("div is 0")

    except Exception:
        print("catch a exception")

    finally:
        print("done")




test = catchExc()


'''
学习点:   try...except   异常捕捉     https://www.runoob.com/python3/python3-errors-execptions.html

'''