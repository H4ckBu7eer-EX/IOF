def run_command(command):
    import subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('gbk')


def getweekpas():
    key = input("输入查询的设备名称：")
    import requests
    url = 'https://www.shentoushi.top/av/Getinfo.php'
    data = {'QueryName': key}

    response = requests.post(url, data=data)
    print(response.text)


def findav():
    key = run_command("tasklist /svc").replace(' ', '+')
    import requests
    url = 'https://www.shentoushi.top/av/av.php'
    data = {'input_process': key}

    response = requests.post(url, data=data)
    print(response.text)


#findav(run_command("tasklist /svc").replace(' ', '+'))
'''
def findcve():
    key = (run_command("systeminfo").replace(' ', '+'))
    import requests
    url = 'https://www.shentoushi.top/av/kb.php'
    data = {'input_process': key}

    response = requests.post(url, data=data)
    print(response.text)
'''