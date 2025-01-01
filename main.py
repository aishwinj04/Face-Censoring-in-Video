import cv2

def analyze_video():
    video = cv2.VideoCapture('assets/video1.mp4')
    success, frame = video.read()
    height = frame.shape[0]
    width = frame.height[1]

    return width, height

def initialize_output():
    
    # create blank video to add frames to

    width, height = analyze_video()
    output = cv2.VideoWriter('assets/output.mp4', cv2.VideoWriter_fourcc(*'mp4'), 30, (width, height))