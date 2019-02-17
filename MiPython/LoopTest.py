import sys
#command=input()
def MiExit(command):
    if command=="exit"or command=="Exit":
        sys.exit()


def checkNum(num):
    try:
       # num = int(input())
        if num % 2 == 0:
            print(num//2)
            return num//2
        else:
            print(3*num+1)
            return 3*num+1
    except TypeError :
       print("请输入正确的数字一个数字")
    except ValueError :
       print("请输入正确的数字一个数字")


def inputNum():
    print("请输入一个数字")
    num = input()
    try:
        num = int(num)
    except TypeError:
        print("输入错误")
    except ValueError:
        print("输入错误")
    return num


def testRange():
    for i in range(0,12,2):#包左不包右
        print(i)

a=inputNum()
while a!=1:
    a=inputNum()
testRange()