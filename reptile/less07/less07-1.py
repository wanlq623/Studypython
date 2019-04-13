import requests

#第一步扇贝选择出题范围
#请求url
web_url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
#模拟请求头部文件
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
#发起请求，将响应结果赋值给变量web_res
web_res = requests.get(web_url,headers=headers)
#打印返回状态，200表示成功
print('请求第一步返回状态为：%s' % web_res.status_code)
#解析返回数据
web_json = web_res.json()
#匹配data后获取数据列表
data_subject = web_json['data']
#定义空列表存储选择的出题范围
choice_list = []
choiceid_list = []
#遍历data_list的长度获取学科
for i in range(len(data_subject)):
    #获取学科名称
    subject_name = data_subject[i][1]
    #获取学科id
    subject_id = data_subject[i][0]
    #添加到choice_list列表
    choice_list.append(subject_name)
    #添加id到choiceid_list列表
    choiceid_list.append(subject_id)

print('第一步：请选择出题范围，输入0-9任意数字。')
print(choice_list)
choice_subject = int(input('请选择：'))
print('你已经选择了" %s "做为测试' % choice_list[choice_subject])
choice_next = input('继续测试请输入"y",回车直接结束。')
if choice_next == 'y':
    # 定义变量category（选择学科id）
    category = choiceid_list[choice_subject]

    # 第二步，根据题库获取单词
    # 请求url
    word_url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?'
    # 模拟请求头部文件
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # 链接后面的请求参数
    word_params = {'category': category}
    # 发起请求，将响应结果赋值给变量word_res
    word_res = requests.get(word_url, params=word_params, headers=headers)
    # 打印返回状态，200表示成功
    print('请求第二步返回状态为：%s' % word_res.status_code)
    # 解析返回数据
    word_json = word_res.json()
    # 匹配data获取单词数据列表
    data_words = word_json['data']
    #定义空字典存放单词的题目
    word_dict = {}#题目选项
    word_dict1 = {}#答案
    #定义空列表存放单词
    list_words = []
    #定义空列表存放单词正确答案id
    right_answers = []
    #定义空列表存放用户选择的单词
    choice_user = []
    #定义空列表存放用户没有选择的单词
    notchoice_user = list_words

    print('------------请看下面的单词--------------')
    #遍历data_words长度
    for x in range(len(data_words)):
        #定义一个题目选项的空字典
        questionchoice_dict = {}
        questionchoice_dict1 ={}
        #定义选项
        choices = ['a','b','c','d']
        #获取单词
        word = data_words[x]['content']
        #获取正确答案id
        right_rank = data_words[x]['rank']
        #获取题目
        word_questions = data_words[x]['definition_choices']
        for num_question in range(len(word_questions)):
            #获取选项的rank值
            rank = word_questions[num_question]['rank']
            #获取选项的内容
            definition = word_questions[num_question]['definition']
            #选项
            choice = choices[num_question]
            #将选项的rank值和内容组成一个字段，rank:definition
            questionchoice_dict1[choice] = rank
            questionchoice_dict[choice] = definition
        #将题目添加到字典，word:questionchoice_dict
        word_dict1[word] = questionchoice_dict1
        word_dict[word] = questionchoice_dict
        #添加列表
        list_words.append(word)
        #添加列表
        right_answers.append(right_rank)
        # print(word_dict1)
        # print(word_dict)
        # print(right_answers)
    #print(word_dict)
    #打印单词，每行5个打印
    for m in range(0,len(list_words),5):
        #打印模版
        temple = '{}    {}    {}    {}    {}'
        #打印内容
        print(temple.format(*list_words[m:m+5]))
    while True:
        choice_contione = input('请输入认识的单词，输入"y"结束输入')
        if choice_contione == 'y':
            break
        else:
            choice_user.append(choice_contione)
            list_words.remove(choice_contione)
    print('你认识的单词的数量：%s,分别是：%s' % (len(choice_user),choice_user))
    #print('你不认识的单词的数量为：%s，分别是：%s' % (len(notchoice_user),notchoice_user))
    print('------------------------做题测评开始------------------------')
    right_num = 0
    wrong_word =[]
    for count in range(len(choice_user)):
        print('第%s题开始：\n' % count+1)
        question = word_dict[choice_user[count]]
        # print(question)
        question_bd = word_dict1[choice_user[count]]
        right_answer = right_answers[count]
        for a,b in question.items():
            print('%s : %s'%(a,b))
        choice_end = input('请选择单词：%s的正确答案(请输入a,b,c,d中的一个)' % choice_user[count])
        # print(question_bd)
        # print(right_answer)
        if question_bd[choice_end] == right_answer:
            right_num +=1
        else:
            wrong_word.append(choice_user[count])

    print('现在，到了公布成绩的时刻:')
    print('在%s个%s词汇当中，你认识其中%s个，实际掌握%s个，错误%s个'%(len(list_words),choice_list[choice_subject],len(choice_user),right_num,len(wrong_word)))

else:
    pass