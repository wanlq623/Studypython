class Survey():
    # 收集调查问卷的答案
    def __init__(self, question):
        self.question = question
        self.response = []

    # 显示调查问卷的题目
    def show_question(self):
        print(self.question)

    # 存储问卷搜集的答案
    def store_response(self, new_response):
        self.response.append(new_response)


# 请定义实名调查问卷的新类 RealNameSurvey，继承自 Survey 类。
class RealNameSurvey(Survey):
    def __init__(self, question):
        Survey.__init__(self, question)
        # 定义收集问卷答案的变量，代码量1行
        self.question = question
        self.response = {}

    # 存储问卷搜集的答案（覆盖父类的类方法）
    def store_response(self, name, new_response):
        self.response[name] = new_response


# 由于存储答案的变量从列表变成字典，因此存储答案的代码需要改变，代码量1行

survey = RealNameSurvey('你的籍贯地是哪？')
survey.show_question()
while True:
    response = input('请回答问卷问题，按 q 键退出：')
    if response == 'q':
        break
    name = input('请输入回答者姓名：')
    # 请将答案用问卷系统存储起来，1 行代码
    survey.store_response(name,response)

# 输出测试
for name, value in survey.response.items():
    print(name + '：' + value)
