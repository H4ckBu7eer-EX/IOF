def dnslog():
    HOST = '0.0.0.0'
    PORT = 53
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print("开启成功...\n使用 nslookup test "+ip_address+"检验")
        while True:
            data, addr = s.recvfrom(2024)
            print(f'Received from {addr}: {data}')