from mod.help import *
from mod.upload import *
from mod.ser import *
from mod.mumaser import *
from mod.shot import *
import random


#启动项===========
upload()
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

ver=1

def print_colorful(text):
    colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m']
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
        ("5", "|whois查询"),
        ("6", "|dns查询"),
        ("7", "|FOFA"),
        ("8", "|SHODAN"),
        ("9", "|ZOOMEYE"),
        ("10", "|ZOOMEYE"),
        ("11", "|ZOOMEYE"),
        ("12", "|ZOOMEYE"),
        ("13", "|ZOOMEYE"),
        ("14", "|ZOOMEYE"),
        ("15", "|ZOOMEYE"),
        ("16", "|ZOOMEYE"),
        ("17", "|ZOOMEYE"),
        ("18", "|ZOOMEYE"),
        ("19", "|ZOOMEYElast"),
    ]
    print(help)
    print("==========菜单==========")
    for i in range(0, 20):
        print(functions_name[i][0].ljust(5) + " " + functions_name[i][1].ljust(15))


def input_com():
    print_menu()
    while True:
        user_input = input('请输入指令: ')
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
        elif user_input == "2":
            print("=====选择exe版本或python版本=====")
            version = input("1| exe版本(完全控制时&界面美观&可选目录)\n2| python版本(隐蔽&自定义)\n输入选择:")
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
            print("f")
        elif user_input == "6":
            print("a")
        elif user_input == "7":
            print("b")
        elif user_input == "8":
            print("c")
        elif user_input == "9":
            print("d")
        elif user_input == "10":
            print("e")
        elif user_input == "11":
            print("f")
        elif user_input == "12":
            print("e")
        elif user_input == "13":
            print("f")
        elif user_input == "14":
            print("a")
        elif user_input == "15":
            print("b")
        elif user_input == "16":
            print("c")
        elif user_input == "17":
            print("d")
        elif user_input == "18":
            print("e")
        elif user_input == "19":
            print("f")
        else:
            print("你输入了预期之外的选项，渗透也是如此。\n不拘泥于工具，不止步于此，少年！")


input_com()