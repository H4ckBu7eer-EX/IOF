def localinfo():
    import socket
    import subprocess
    print("\033[1;31m=====探测机器本地信息=====\033[0m")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("当前IP地址为: ", "\033[1;32m", ip_address, "\033[0m")
    whoami = subprocess.check_output(['whoami']).decode('utf-8').strip()
    print("当前用户为:", "\033[1;32m", whoami, "\033[0m")

def get_env():
    import os
    env=os.environ
    print("=====环境变量=====\n"+str(env))

def check_ip():
    import requests
    import json
    print("\033[1;31m=====探测机器出网信息=====\033[0m")
    try:
        response = requests.get('http://ip-api.com/json/')
        if response.status_code:
            data = json.loads(response.text)
            new_data = {
                "IP": data["query"],
                "国家": data["country"],
                "城市": data["city"],
                "服务商": data["isp"],
                "公司": data["org"]
            }
            print("\033[1;31m=====ip-api信息=====\033[0m")
            print("\033[1;30m" + json.dumps(new_data, indent=4, ensure_ascii=False) + "\033[0m")
    except:
        print('\033[1;32m=====此机器不出网=====\033[0m')

'''
def systeminfo():
    import subprocess
    sysinfo = subprocess.check_output(['systeminfo']).decode('gbk').strip()
    return sysinfo


def netstat():
    import subprocess
    netstat = subprocess.check_output(['tasklist /svc']).decode('gbk').strip()
    return netstat
'''

