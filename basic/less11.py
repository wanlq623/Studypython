# 创建一个人事系统类
class hrSystem:
    # 创建存储员工名字的变量 name
    name = ''
    # 创建存储员工工资的变量 salary
    salary = 0
    # 创建存储员工绩效的变量 kpi
    kpi = 0

    # 定义录入员工信息的类方法
    @classmethod
    def record(cls, name, salary, kpi):
        cls.name = name
        cls.salary = salary
        cls.kpi = kpi

    # 定义打印员工信息的类方法
    @classmethod
    def print_record(cls):
        if cls.check_name():
            print(cls.name + '的工作信息如下：')
            print('本月工资：' + str(cls.salary))
            print('本年绩效：' + str(cls.kpi))

    # 定义根据 kpi 评奖的类方法
    @classmethod
    def kpi_reward(cls):
        if cls.kpi > 95:
            print('恭喜' + cls.name + '拿到明星员工奖杯！')
        elif cls.kpi <= 95 and cls.kpi >= 80:
            print('恭喜' + cls.name + '拿到优秀员工奖杯！')
        else:
            print('很遗憾' + cls.name + '这次没有评上奖杯，希望来年努力工作，勇创佳绩！')

    # 检查录入名称是否正确的类方法
    @classmethod
    def check_name(cls):
        if cls.name not in ['bob', 'candy', 'jony', 'kelly']:
            print('录入错误！' + cls.name + '不是本公司员工！')
            return 0
        else:
            print('录入正确~')
            return 1


# 验证结果的代码
hrSystem.record('spy', 3000, 60)
hrSystem.print_record()
