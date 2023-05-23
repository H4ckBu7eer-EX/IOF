def getweekpas(key):
    import requests
    url = 'https://www.shentoushi.top/av/Getinfo.php'
    data = {'QueryName': key}

    response = requests.post(url, data=data)
    print(response.text)


def findav(key):
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