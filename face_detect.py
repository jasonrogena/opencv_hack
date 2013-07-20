import time
from cv2_detect import detect
import cv2
import cv2.cv as cv
import sys
import os
import glob
 
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
def faces(in_fn, out_dir):
    print ">>> Loading image..."
    #time.sleep(0.2)
    img_color = cv2.imread(in_fn)
    img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
 
    print ">>> Detecting faces in "+in_fn
    rects = detect(img_gray)
    print "faces detected: ", len(rects)
    if not len(rects)==0:
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
		if not out_dir.endswith("/"):
			out_dir=out_dir+"/"
		img_out = img_color.copy()
		draw_rects(img_out, rects, (0, 255, 0))
		cv2.imwrite(out_dir+in_fn, img_out)
    else:
        miss_file="miss/"
        if not os.path.exists(miss_file):
            os.makedirs(miss_file)
        cv2.imwrite(miss_file+in_fn, img_color)
 
def main():
    #demo('pic.jpg', 'pic_detected.jpg')
    #file_type original_dir result_dir
    if len(sys.argv)>=3:
		print "starting..."
		file_type=sys.argv[1]
		original_dir=sys.argv[2]
		result_dir=sys.argv[3]
		os.chdir(original_dir)
		for files in os.listdir("."):
			if files.endswith(file_type):
				faces(files,result_dir)
 
if __name__ == '__main__':
    main()
