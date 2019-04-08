#文字小游戏V2.0版
import random,time

# 需要的数据和变量
player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
enemy_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】']
players = random.sample(player_list,3)
enemys = random.sample(enemy_list,3)
players_info = {}
enemys_info = {}

# 随机生成角色的属性
def born_role():
    life = random.randint(100,300)
    attack = random.randint(1,100)
    return life,attack

# 生成和展示角色信息
def show_role():

    print('我方英雄信息：')
    print('----------------')
    for i in range(3):
        players_info[players[i]] = born_role()

        print('%s 血量：%d 攻击：%d' % (players[i],players_info[players[i]][0],players_info[players[i]][1]))
        time.sleep(1.5)
    print('---------------')
    time.sleep(1.5)
    print('敌方英雄信息：')
    print('----------------')
    for i in range(3):

        enemys_info[enemys[i]] = born_role()
        print('%s 血量：%d 攻击：%d' % (enemys[i], enemys_info[enemys[i]][0], enemys_info[enemys[i]][1]))
        time.sleep(1.5)
    print('---------------')
    time.sleep(1.5)
    input('请按回车键继续。\n')

# 角色排序，选择出场顺序。
def order_role():
    global players
    choice_dict = {}
    for i in range(3):
        choice = int(input('你想将 %s 放在第几个上场？(输入数字1~3)' % players[i]))
        choice_dict[choice] = players[i]

    players = []
    for i in range(1,4):
        players.append(choice_dict[i])

    print('\n我方角色的出场顺序是：%s、%s、%s' % (players[0], players[1], players[2]))
    time.sleep(1.5)
    print('敌方角色的出场顺序是：%s、%s、%s' % (enemys[0], enemys[1], enemys[2]))
    time.sleep(1.5)

# 角色PK
def pk_role():
    round = 1
    score = 0

    for i in range(3):
        player_name = players[i]
        enemy_name = enemys[i]
        player_life = players_info[players[i]][0]
        enemy_life = enemys_info[enemys[i]][0]
        player_attack = players_info[players[i]][1]
        enemy_attack = enemys_info[enemys[i]][1]
        #player_life = player_life - enemy_attack
        #enemy_life = enemy_life - player_attack

        print('\n----------------- 【第%d局】 -----------------' % round)
        print('玩家角色：%s vs 敌方角色：%s' % (player_name,enemy_name))
        time.sleep(1.5)
        print('%s 血量：%d  攻击：%d' % (player_name,player_life,player_attack))
        time.sleep(1.5)
        print('%s 血量：%d  攻击：%d' % (enemy_name,enemy_life,enemy_attack))
        time.sleep(1.5)
        input('请按回车键继续。\n')

        while player_life > 0 and enemy_life > 0:
            player_life = player_life -enemy_attack
            enemy_life = enemy_life - player_attack
            print('%s发起了攻击，%s剩余血量%d' % (player_name,enemy_name,enemy_life))
            time.sleep(1.5)
            print('%s发起了攻击，%s剩余血量%d' % (enemy_name,player_name,player_life))
            time.sleep(1.5)
            print('------------------------------------')
            time.sleep(1.5)
        else:
            print(show_result(player_life,enemy_life)[1])

            score = int(show_result(player_life,enemy_life)[0])
        round += 1

    input('\n点击回车，查看比赛的最终结果\n')
    if score > 0:
        print('【最终结果：你赢了！】\n')
    elif score < 0:
        print('【最终结果：你输了！】\n')
    else:
        print('【最终结果：平局！】\n')




# 返回单局战果和计分法所加分数。
def show_result(player_life, enemy_life):

    if player_life > 0 and enemy_life <= 0:
        result = '\n敌人死翘翘了，你赢了！'
        return 1,result

    elif player_life <= 0 and enemy_life > 0:
        result = '\n悲催，敌人把你干掉了！'
        return -1,result

    else:
        result = '\n哎呀，你和敌人同归于尽了！'
        return 0,result


# （主函数）展开战斗流程
def main():
    show_role()
    order_role()
    pk_role()


# 启动程序（即调用主函数）
main()


#教材参考代码
# import time, random
#
# # 需要的数据和变量放在开头
# player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
# enemy_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】']
# players = random.sample(player_list, 3)
# enemies = random.sample(enemy_list, 3)
# player_info = {}
# enemy_info = {}
#
#
# # 随机生成角色的属性
# def born_role():
#     life = random.randint(100, 180)
#     attack = random.randint(30, 50)
#     return life, attack
#
#
# # 生成和展示角色信息
# def show_role():
#     for i in range(3):
#         player_info[players[i]] = born_role()
#         enemy_info[enemies[i]] = born_role()
#
#     # 展示我方的3个角色
#     print('----------------- 角色信息 -----------------')
#     print('你的人物：')
#     for i in range(3):
#         print('%s  血量：%d  攻击：%d'
#               % (players[i], player_info[players[i]][0], player_info[players[i]][1]))
#     print('--------------------------------------------')
#     print('电脑敌人：')
#
#     # 展示敌方的3个角色
#     for i in range(3):
#         print('%s  血量：%d  攻击：%d'
#               % (enemies[i], enemy_info[enemies[i]][0], enemy_info[enemies[i]][1]))
#     print('--------------------------------------------')
#     input('请按回车键继续。\n')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。
#
#
# # 角色排序，选择出场顺序。
# def order_role():
#     global players
#     order_dict = {}
#     for i in range(3):
#         order = int((input('你想将 %s 放在第几个上场？(输入数字1~3)' % players[i])))
#         order_dict[order] = players[i]
#
#     players = []
#     for i in range(1, 4):
#         players.append(order_dict[i])
#
#     print('\n我方角色的出场顺序是：%s、%s、%s' % (players[0], players[1], players[2]))
#     print('敌方角色的出场顺序是：%s、%s、%s' % (enemies[0], enemies[1], enemies[2]))
#
#
# # 角色PK
# def pk_role():
#     round = 1
#     score = 0
#     for i in range(3):  # 一共要打三局
#         player_name = players[i]
#         enemy_name = enemies[i]
#         player_life = player_info[players[i]][0]
#         player_attack = player_info[players[i]][1]
#         enemy_life = enemy_info[enemies[i]][0]
#         enemy_attack = enemy_info[enemies[i]][1]
#
#         # 每一局开战前展示战斗信息
#         print('\n----------------- 【第%d局】 -----------------' % round)
#         print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
#         print('%s 血量：%d  攻击：%d' % (player_name, player_life, player_attack))
#         print('%s 血量：%d  攻击：%d' % (enemy_name, enemy_life, enemy_attack))
#         print('--------------------------------------------')
#         input('请按回车键继续。\n')
#
#         # 开始判断血量是否都大于零，然后互扣血量。
#         while player_life > 0 and enemy_life > 0:
#             enemy_life = enemy_life - player_attack
#             player_life = player_life - enemy_attack
#             print('%s发起了攻击，%s剩余血量%d' % (player_name, enemy_name, enemy_life))
#             print('%s发起了攻击，%s剩余血量%d' % (enemy_name, player_name, player_life))
#             print('--------------------------------------------')
#             time.sleep(1)
#         else:  # 每局的战果展示，以及分数score和局数的变化。
#             # 调用show_result()函数，打印返回元组中的result。
#             print(show_result(player_life, enemy_life)[1])
#             # 调用show_result()函数，完成计分变动。
#             score += int(show_result(player_life, enemy_life)[0])
#             round += 1
#     input('\n点击回车，查看比赛的最终结果\n')
#
#     if score > 0:
#         print('【最终结果：你赢了！】\n')
#     elif score < 0:
#         print('【最终结果：你输了！】\n')
#     else:
#         print('【最终结果：平局！】\n')
#
#
# # 返回单局战果和计分法所加分数。
# def show_result(player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
#     if player_life > 0 and enemy_life <= 0:
#         result = '\n敌人死翘翘了，你赢了！'
#         return 1, result  # 返回元组(1,'\n敌人死翘翘了，你赢了！')，类似角色属性的传递。
#     elif player_life <= 0 and enemy_life > 0:
#         result = '\n悲催，敌人把你干掉了！'
#         return -1, result
#     else:
#         result = '\n哎呀，你和敌人同归于尽了！'
#         return 0, result
#
#
# # （主函数）展开战斗流程
# def main():
#     show_role()
#     order_role()
#     pk_role()
#
#
# # 启动程序（即调用主函数）
# main()