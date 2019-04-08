# 请你改造下面的代码，目标：不论输入了什么，程序都不会因报错而停止（即找到所有的报错类型）。

while True:
    print('\n欢迎使用除法计算器！\n')
    try:
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x)/float(y)
        # 下面是 print函数的一种用法，用逗号隔开，可在同一行打印不同类型的数据。
        print(x, '/', y, '=', z)
        break  # 当成功运行一次除法运算后，退出程序。
    except ZeroDivisionError:
        print('0是不能做除数的')

    except TypeError:
        print('输入了非数值')

    except ValueError:
        print('数值为空')
