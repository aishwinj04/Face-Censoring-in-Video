import cv2

def analyze_video(video_path):
    success, frame = video_path.read()
    if success:
        height = frame.shape[0]
        width = frame.shape[1]

    return success, frame, width, height

def initialize_output(width, height):
    
    # create blank video to add frames to
    output = cv2.VideoWriter('assets/output.mp4', cv2.VideoWriter_fourcc(*'mp4'), 30, (width, height))
    return output

def main():
    video = cv2.VideoWriter('assets/video1.mp4')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    success, frame, width, height = analyze_video(video)

    output = initialize_output(width, height)

    while success:
        faces = face_cascade.detectMultiScale(frame, 1.1, 6)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,255),9)

        output.write(frame)

        # get next frame
        success, frame, width, height = analyze_video(video)

    video.release()
    output.release()
    cv2.destroyAllWindows




