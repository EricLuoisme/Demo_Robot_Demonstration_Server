import os
# import AutoWeb
from NAudioProcess.data import File_Setting
from NAudioProcess import NMain_process


# 用于对存储的语音合成的mp3文件进行命名，由于在win10中覆盖音频文件权限不足
FILE_NUMBER = 0


##############################################################################
def determine_scenario(string):

    """
    函数接受 string 字符串并进行场景判断，最后调用 NAudioProcess.data 中的

    """

    global FILE_NUMBER

    # 判断是否存在路径，没有则创建
    if os.path.exists(File_Setting.outPath_Combin) is False:
        os.makedirs(File_Setting.outPath_Combin)

    return_state = NMain_process.identify_execute(string, FILE_NUMBER, True)
    if return_state is not None:
        FILE_NUMBER = FILE_NUMBER + 1
################################################################################

# real start point of the program #

# AutoWeb.login() #提前打开浏览器完成登录操作

# string = str("请制作一张提现凭证")
# determine_scenario(check, string)

# here for receiving the message from the robot




