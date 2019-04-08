import random


food_list = ['小鸡炖蘑菇','鱼香茄子','麻婆豆腐','蒜蓉青菜','水煮牛肉','酸菜鱼','小炒肉','大盆花菜','卤味拼盘','白切鸡','炭火烤鸡','深井烧鹅','明炉烧鸭',]

food_todaty = []

what_eate = input('知道今天吃什么么？知道输入Y，不知道输入N')

if what_eate == 'Y':
    while True:
        food = input('请输入今天要吃的菜')
        food_todaty.append(food)
        con = input('是否继续输入，是请输入Y，否请输入N')
        if con == 'N':
            print('今天要吃的菜有：%s'%food_todaty)
            break
        else:
            continue
else:
    while True:
        food_todaty = random.sample(food_list,3)
        print('今天准备的菜谱有：%s'%food_todaty)
        what_yn = input('这些菜谱是否满意，满意请输入Y，不满意请输入N')
        if what_yn == 'Y':
            print('今天要吃的菜有：%s'%food_todaty)
            break
        else:
            continue
