import cv2

def analyze_video():
    video = cv2.VideoCapture('assets/video1.mp4')
    success, frame = video.read()
    height = frame.shape[0]
    width = frame.height[1]

    return width, height

