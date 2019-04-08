#文字小游戏V3.0版

import random
import time


# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name):
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):
        Role.__init__(self, name)  # 继承了父类的初始化函数，所以，self.name = name 不用重复写。
        self.life = self.life * 5
        self.attack = self.attack * 3


class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5


class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4


# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game():
    def __init__(self):
        # 初始化各种变量
        self.players = []  # 存玩家顺序
        self.enemies = []  # 存敌人顺序
        self.score = 0  # 比赛积分
        self.i = 0  # 记轮次
        # 执行各种游戏函数
        self.game_start()  # 欢迎语
        self.born_role()  # 随机生成6个角色
        self.show_role()  # 展示角色
        self.order_role()  # 排序并展示
        self.pk_role()  # 让双方 Pk 并展示结果
        self.show_result()  # 展示最终结局

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“PK小游戏” ------------')
        print('将自动生成【你的队伍】和【敌人队伍】')
        input('请按回车键继续。')

    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(), Assassin(), Bowman()]))
            self.enemies.append(random.choice([Knight(), Assassin(), Bowman()]))

    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('『我方』%s 血量：%s  攻击：%s' %
                  (self.players[i].name, self.players[i].life, self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s' %
                  (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')

    # 排序并展示
    def order_role(self):
        order_dict = {}
        for i in range(3):
            order = int(input('你想将 %s 放在第几个上场？(输入数字1~3)' % self.players[i].name))
            order_dict[order] = self.players[i]
        self.players = []
        for i in range(1, 4):
            self.players.append(order_dict[i])
        print('\n你的队伍出场顺序是：%s、%s、%s'
              % (self.players[0].name, self.players[1].name, self.players[2].name))
        print('敌人队伍出场顺序是：%s、%s、%s'
              % (self.enemies[0].name, self.enemies[1].name, self.enemies[2].name))

    # 让双方 Pk 并展示结果
    def pk_role(self):
        for i in range(3):
            print('\n----------------- 【第%s轮】 -----------------' % (i + 1))
            # 每一局开战前加buff
            input('\n战斗双方准备完毕，请按回车键继续。')
            print('--------------------------------------------')

            while self.players[i].life > 0 and self.enemies[i].life > 0:
                self.enemies[i].life -= self.players[i].attack
                self.players[i].life -= self.enemies[i].attack
                print('我方%s 发起了攻击，敌方%s 剩余血量 %s' %
                      (self.players[i].name, self.enemies[i].name, self.enemies[i].life))
                print('敌方%s 发起了攻击，我方%s 剩余血量 %s' %
                      (self.enemies[i].name, self.players[i].name, self.players[i].life))
                print('--------------------------------------------')
                time.sleep(1)
            if self.players[i].life <= 0 and self.enemies[i].life > 0:
                print('\n很遗憾，我方%s 挂掉了！' % (self.players[i].name))
                self.score -= 1
            elif self.players[i].life > 0 and self.enemies[i].life <= 0:
                print('\n恭喜，我方%s 活下来了。' % (self.players[i].name))
                self.score += 1
            else:
                print('\n我的天，他们俩都死了啊！')

    # 展示最终结局
    def show_result(self):
        input('\n请按回车查看最终结果。\n')
        if self.score > 0:
            print('【最终结果】\n你赢了！')
        elif self.score == 0:
            print('【最终结果】\n平局。')
        else:
            print('【最终结果】\n你输了。')


gp = Game()