#文字小游戏V1.0版
import time,random

player_victory = 0 #定义变量存放玩家获胜局数
enemy_victory = 0 #定义变量存放敌方获胜局数
while True:
#战斗三局
    for i in range(1,4):
        time.sleep(2)
        print('\n------------现在是第 %s 局--------------' %i)


        player_life = random.randint(100,150) #定义玩家血量随机在100-150之间
        player_attack = random.randint(30,50) #定义玩家攻击力随机在30-50之间
        enemy_life = random.randint(100,150) #定义敌方血量随机在100-150之间
        enemy_attack = random.randint(30,50) #定义敌方攻击力随机在30-50之间

        #打印双方属性
        print('【玩家】\n 血量：%s \n 攻击力：%s' % (player_life,player_attack))
        print('---------------------------------')
        time.sleep(1.5)
        print('【敌方】\n 血量：%s \n 攻击力：%s' % (enemy_life,enemy_attack))
        print('---------------------------------')
        time.sleep(1.5)

        #战斗开始,只要双方血量大于0就一直战斗
        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack #计算每次战斗玩家血量剩余
            enemy_life = enemy_life - player_attack #计算每次战斗敌方血量剩余
            print('你发起了攻击，【敌方】剩余血量 %s' % enemy_life)
            print('敌方向你发起了攻击，【玩家】剩余血量 %s' % player_life)
            print('---------------------------------')
            time.sleep(1.5)

        #打印战斗结果
        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')

        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')

        else:
            print('哎呀，你和敌人同归于尽了！')

    #双方pk结果

    if player_victory > enemy_victory:
        print('【最终结果：你赢了！】')
    elif player_victory < enemy_victory:
        print('【最终结果：你输了！】')
    else:
        print('【最终结果：平局！】')

    #询问是否还要继续游戏
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break
