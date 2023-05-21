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
    ip = input('输入IP: ') or '127.0.0.1'
    port = input('输入端口: ') or 22
    user = input('输入用户名: ')
    password = input('输入密码: ')
    cmd = input('输入执行的命令： ') or 'whoami'
    ssh_command(ip, port, user, password, cmd)


def ssh_server():
    import os
    import paramiko
    import socket
    import sys
    import threading

    CWD = os.path.dirname(os.path.realpath(__file__))
    HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'rsa.key'))


    class Server (paramiko.ServerInterface):
        def _init_(self):
            self.event = threading.Event()

        def check_channel_request(self, kind, chanid):
            if kind == 'session':
                return paramiko.OPEN_SUCCEEDED
            return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

        def check_auth_password(self, username, password):
            if (username == 'tim') and (password == 'sekret'):
                return paramiko.AUTH_SUCCESSFUL


    if __name__ == '__main__':
        server = '0.0.0.0'
        ssh_port = 2222
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((server, ssh_port))
            sock.listen(100)
            print('[+] 等待连接 ...')
            client, addr = sock.accept()
        except Exception as e:
            print('[-] 连接失败: ' + str(e))
            sys.exit(1)
        else:
            print(f'[+]  {addr}，已连接')

        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(HOSTKEY)
        server = Server()
        bhSession.start_server(server=server)

        chan = bhSession.accept(20)
        if chan is None:
            print('*** 没有会话')
            sys.exit(1)

        print('[+] Authenticated!')
        print(chan.recv(1024).decode())
        chan.send('ssh connect!')
        try:
            while True:
                command = input("GOGOGO>> ")
                if command != 'exit':
                    chan.send(command)
                    r = chan.recv(8192)
                    print(r.decode())
                else:
                    chan.send('exit')
                    print('=====退出=====')
                    bhSession.close()
                    break
        except KeyboardInterrupt:
            bhSession.close()