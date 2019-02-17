def collatz(va):
    try:
      num=  int(va);
      if  int(num%2)==0:
          return num//2;
      else:
          return 3*num+1;
    except TypeError:
        print("请输入一个数字")
        return 1
    except ValueError:
        print("请输入一个数字")
        return 1


num =input()
while(num!=1):
    print("当前的数字："+str(num))
    if num==1:
        print("请输入一个不等于1的数数字")
    num=collatz(num)

print("操作执行完成："+str(num))
#DEMO  完成