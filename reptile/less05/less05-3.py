import requests

#获取快递公司的值
def get_company(courier_number):
    #查下获取快递公司的url
    company_url = 'https://www.kuaidi100.com/autonumber/autoComNum?'
    #模拟请求头文件
    company_headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'WWWID=WWWB8B476ECBFC68CC9AF2FC3CF07F6B9D1',
        'Host': 'www.kuaidi100.com',
        'Origin': 'https://www.kuaidi100.com',
        'Referer': 'https://www.kuaidi100.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    #url后面的参数
    company_params = {
        'resultv2': '1',
        'text': courier_number
    }

    # 返回一个response对象，赋值给res_company
    res_company = requests.get(company_url, params=company_params, headers=company_headers)
    # 打印返回状态
    print('请求获取快递公司返回状态：' + str(res_company.status_code))
    print('-------------返回状态分割线---------------')
    # 使用json()方法，将response对象，转为列表/字典
    company_json = res_company.json()

    company_lists = company_json['auto']

    company_types = []

    for company in company_lists:
        company_type = company['comCode']
        company_types.append(company_type)
    return company_types

#获取快递流程跟踪
def get_process(company_type,courier_number):
    process_url = 'https://www.kuaidi100.com/query?'
    process_headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection': 'keep - alive',
        'Cookie': 'WWWID = WWWB8B476ECBFC68CC9AF2FC3CF07F6B9D1',
        'Host': 'www.kuaidi100.com',
        'Referer': 'https://www.kuaidi100.com /',
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest'
    }
    process_params = {
        'type': company_type,
        'postid': courier_number,
        'temp': '0.2887579092844803',
        'phone': ''
    }
    #print(process_params)

    # 返回一个response对象，赋值给res_music
    res_process = requests.get(process_url, params=process_params, headers=process_headers)
    # 打印返回状态
    print('请求获取快递公司返回状态：' + str(res_process.status_code))
    print('-------------返回状态分割线---------------')
    # 使用json()方法，将response对象，转为列表/字典
    process_json = res_process.json()

    process_lists = process_json['data']

    for process in process_lists:
        process_context = process['context']
        process_time = process['time']
        print('时间：%s地点和跟踪进度：%s\n'%(process_time,process_context))

#调用函数
courier_number = input('请输入要查下的快递单号：')
companys = get_company(courier_number)
print('查询到的快递公司有：%s'%companys)
company_type = input('请直接根据查询出的结果输入快递公司')
get_process(company_type,courier_number)


# res_process = requests.get('https://www.kuaidi100.com/query?type=ems&postid=1085160751132&temp=0.5647948381475716&phone=')
#
# process_json = res_process.json()
#
# process_lists = process_json['data']
#
# for process in process_lists:
#
#     process_context = process['context']
#
#     process_time = process['time']
#
#     print('时间：%s地点和跟踪进度：%s\n'%(process_time,process_context))

