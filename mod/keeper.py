import psutil

for proc in psutil.process_iter():
    print(proc.name(), proc.pid)

pid = input('请输入进程PID: ')
try:
    proc = psutil.Process(int(pid))
    print("=====尝试维持=====")
    p = psutil.Process(int(pid))
    exe_path = p.exe()
    print(exe_path)
except psutil.NoSuchProcess:
    print("=====进程不存在=====")