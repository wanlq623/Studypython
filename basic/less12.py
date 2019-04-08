# 请根据所学，补全以下代码：

class calendar:
    # 日程表的日期
    date = '2020-08-08'
    # 事件清单，以字典形式给出，键为事件，值是安排的时间
    things = {'给父母买礼物':'9:00', '学习':'10:00', '和朋友聚会':'18:30'}
    @classmethod
    def thing_done(cls,done):
        cls.done = done
        #for cls.done in calendar.things:
        if cls.done in calendar.things:
            del calendar.things[cls.done]
            #print(calendar.things)


    @classmethod
    def add_thing(cls,ndone,xiaoshi):
        cls.ndone = ndone
        cls.xiaoshi = xiaoshi
        #for ndone in calendar.things:
        if cls.ndone not in calendar.things:
            calendar.things[cls.ndone] = cls.xiaoshi
            #print(calendar.things)



calendar.thing_done('给父母买礼物')
calendar.add_thing('写日记', '20:00')
print(calendar.things)
