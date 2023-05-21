def ssh_command(ip, port, user, passwd, cmd):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print("=====返回结果=====")
        for line in output:
            print(line.strip())

def run_1():
    ip = input('Enter server IP: ') or '127.0.0.1'
    port = input('Enter port or <CR>: ') or 22
    user = input('输入用户名: ')
    password = input('输入密码: ')
    cmd = input('输入执行的命令： ') or 'whoami'
    ssh_command(ip, port, user, password, cmd)


def ssh_server():
    pass