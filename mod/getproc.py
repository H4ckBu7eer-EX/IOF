import win32gui
#import win32process


def get_windows():
    handle = win32gui.GetForegroundWindow()
    return handle


def get_all_windows():
    handles = []
    win32gui.EnumWindows(lambda hwnd, handles: handles.append(hwnd), handles)
    return handles


def get_title(handle):
    title = win32gui.GetWindowText(handle)
    return title

"""
def get_pid(hwnd):
    pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid

def get_name(pid):
    process_handle = win32process.OpenProcess(1, False, pid)
    return win32process.GetModuleFileNameEx(process_handle, 0)
"""