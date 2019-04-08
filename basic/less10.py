import csv
#调用open()函数打开csv文件，传入参数：文件名assets.csv，追加模式a，newline=''
with open('assets.csv','a',newline='') as csvfile:
    #用csv.writer()函数创建一个writer对象
    writer = csv.writer(csvfile,dialect='excel')
    #定义表头参数
    header = ['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    #用writerow()函数将表头写进cvs文件
    writer.writerow(header)

unit_loop = True
while unit_loop:
    title=input('请输入小区名称：')
    address = input('请输入小区地址：')
    year = input('请输入小区建造年份：')
    block = input('请输入楼栋号：')
    unit=input('请输入单元号：')

    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')

    input('接下来请依次输入起始层每个房间的户室尾号、南北朝向及面积，按任意键继续')

    #收集起始层的房间信息
    start_floor_rooms = {}
    floor_last_number = []

    #定义循环控制量

    room_loop = True
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号：（如01、02）')
        # 将尾号用append()函数添加到列表里面
        floor_last_number.append(last_number)
        # 户室号为room_number,由楼层start_floor和尾号last_number组成
        room_number = int(start_floor + last_number)

        direction = input('请输入 %d 的朝向（南北朝向输入1，东西朝向输入2）：' % room_number)
        area = input('请输入 %d 的面积，单位㎡ ：' % room_number)
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}
        start_floor_rooms[room_number] = [direction,area]

        continued = input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')

        #判断continued为n时，循环结束
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True
    #print(start_floor_rooms)
    #新建一个放单元所有户室数据的字典
    unit_rooms = {}
    #创建初始楼层的字典模版
    unit_rooms[start_floor] = start_floor_rooms
    #遍历除初始楼层外的其它楼层
    for floor in range(int(start_floor) + 1 , int(end_floor) + 1):
        #每个楼层都建立一个字典
        floor_rooms = {}
        #遍历每层有多少个房间
        for i in range(len(start_floor_rooms)):
            number = str(floor) + floor_last_number[i]
            #依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            #给字典floor_rooms添加键值对，floor_rooms = {401: [1, 80]}
            floor_rooms[int(number)] = info
        unit_rooms[floor] = floor_rooms

    with open('assets.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for sub_dict in unit_rooms.values():
            for room, info in sub_dict.items():
                dire = ['', '南北', '东西']
                writer.writerow([title, address, year, block, unit, room, info[0], info[1]])

    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True
print('恭喜你，资产录入工作完成！')



