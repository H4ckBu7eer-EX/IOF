def check_cameras():
    from cv2 import VideoCapture, imwrite
    camera = VideoCapture(0)
    num_cameras = 0
    if camera.isOpened():
        num_cameras += 1
        camera.release()
        camera = VideoCapture(num_cameras)
        print("\033[32m" + f"检测到{num_cameras}个摄像头!" + "\033[0m")
    else:
        print("\033[31m没有检测到摄像头!\033[0m")
        exit()


def shot():
    from cv2 import VideoCapture, imwrite
    use = input("请输入使用的摄像头编号: ")
    cap = VideoCapture(int(use))
    ret, frame = cap.read()
    imwrite('./shot.png', frame)
    print("\033[32m" + "照片保存至当前目录!" + "\033[0m")

shot()