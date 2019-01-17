
from NAudioProcess import Server
import time


def running():
    """
    总账第三个场景，负责演示对本期提交的凭证进行提交处理，包含查询是否出现
    以及查询错误的子场景

    :return: 不返回任何值
    """
    Server.send('财务凭证提交处理的机器人手部与口头操作')
    print('执行财务凭证提交处理') ## 判断是否成功执行操作 ##
    check = True

    if check is False:
        print('全部凭证提交结束')
        Server.send('场景结束')
    else:
        print('有误，是否查看错误原因')
        Server.send('进入该场景下的子场景')

        receive = Server.receive(True)

        if receive.__contains__('超时') or receive.__contains__('我不'):
            print('提前结束场景')
            Server.send('场景结束')
        elif receive.__contains__('好'):
            print('执行查看操作')
            Server.send('执行查看操作，随后场景结束')
