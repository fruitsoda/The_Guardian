import cv2
import time

def set_mp4(lst, s, fps, w, h, countDetect):
    print("makeVid!!!!!!!:",s)
    out = cv2.VideoWriter("./web/video/"+s+".mp4",cv2.VideoWriter_fourcc(*'X264'), fps, (w,h))
    for im in lst:
        out.write(im)

