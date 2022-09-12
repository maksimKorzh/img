#!/usr/bin/python3

############################################
#
#       Simple script to display images
#
#                    by
#
#             Code Monkey King
#
############################################

# import package
import cv2, sys

# open image
try:
  filename = sys.argv[1]
  img = cv2.imread(sys.argv[1])
  cv2.namedWindow(filename, flags=cv2.WINDOW_GUI_NORMAL)
  cv2.resizeWindow(filename, img.shape[1], img.shape[0])
except Exception as e:
  print(e)
  print('Usage: python3 img.py your-image.png')

# display image
while True:
  cv2.imshow(filename, img)
  keyCode = cv2.waitKey(1)

  if cv2.getWindowProperty(filename, cv2.WND_PROP_VISIBLE) <1:
    break

cv2.destroyAllWindows()
