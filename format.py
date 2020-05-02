import os
import cv2

imgs = os.listdir(".")
ct = 1

for im in imgs:
	if ".html" in im or ".js" in im or ".py" in im: continue
	try:
		img = cv2.imread(im)
		w = img.shape[0]
		h = img.shape[1]
		print(img.shape)
		f = 320/w
		if h > w: f = 320/h
		w = int(f*w) 
		h = int(f*h)
		img = cv2.resize(img, (h,w), interpolation = cv2.INTER_CUBIC)
		print(img.shape)
		cv2.imwrite("%d_new.jpg" % ct, img) 
		ct += 1
	except: continue
