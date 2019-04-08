# 函数会返回一个扑克牌列表，里面有52个元组（将花色和数字分开），对应52张牌。

def cards():
    colors = ['红桃','方块','黑桃','梅花']
    list1 = list(range(2,11))
    list1.extend('JQKA')
    list2 = [(m,n) for m in list1 for n in colors]
    return list2
print(cards())

# # 为了写出优雅的代码，请先学会下面的3个新知识。
# '''
# # 知识1：一种新的列表生成方式
# num1 = [1,2,3,4,5]  # 想一想，如果用这个方法生成一个1-100的列表……
# num2 = list(range(1,6))
# print(num1)
# print(num2)
#
# # 知识2：extend 的新用法
# num2.extend(['ABCDE'])
# num2.extend('ABCDE')  # extend后面是列表的话会将其合并，后面是字符串的话会将每个字符当成一个列表中的元素。
# print(num2)
#
# # 知识点3：列表生成式
# list1 = [i for i in range(1,11)]  # 规定列表中元素的范围
# print(list1)
# list2 = [m+n for m in ['J', 'Q','K'] for n in ['梅花','方块','红桃','黑桃']]  # 列表元素可以是组合，分别规定范围。
# print(list2)
# list4 = [a+b for a in str(list1) for n in ['梅花','方块','红桃','黑桃']]
# list3 = [n*n for n in range(1,11) if n % 3 == 0]  # 元素既可规定范围，也可附加条件。
# print(list3)
# '''
# # 假设用普通的方法来生成上面的列表：
#
# list1 = []
# for i in range(1,11):
#     list1.append(i)
# print(list1)
#
# list2 = []
# for m in list1:
#     for n in ['y','n']:
#         list2.append(str(m)+str(n))
# print(list2)
#
# list3 = []
# for i in range(1,11):
#     if i % 3 == 0:
#         list3.append(i*i)
# print(list3)
#
