def exeser():
    import os
    import subprocess
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = input("请输入共享的目录（建议根目录如'C:\\'）：")
    run="start "+dir_path+"\chfs.exe --path="+dir
    output = subprocess.Popen(run, stdout=subprocess.PIPE, shell=True)
    #print(output.communicate()[0].decode('utf-8'))
    print("尝试访问 http://"+ip_address+" 进行内网传输文件")


def pyser():
    import http.server
    import socketserver
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    PORT = input("请输入端口号(尝试避免常用端口)：")
    while not PORT.isdigit():
        PORT = input("端口号必须是数字，请重新输入：")
    PORT = int(PORT)
    local_ip = socket.gethostbyname(socket.gethostname())
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("服务端口:", PORT, ", 服务地址:", local_ip)
        print("尝试访问 http://"+ip_address+":"+str(PORT)+" 进行内网传输文件")
        httpd.serve_forever()