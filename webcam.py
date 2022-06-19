#!/usr/bin/python3

from cv2 import CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, VideoCapture, imshow, waitKey, destroyAllWindows

if __name__ == "__main__":

    vid = VideoCapture(0)
    vid.set(CAP_PROP_FRAME_WIDTH, 640)
    vid.set(CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        ret, frame = vid.read()
        imshow('Webcam', frame)
        if waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    destroyAllWindows()

