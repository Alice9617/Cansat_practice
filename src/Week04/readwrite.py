import cv2 
filepath=""
img=cv2.imread(filepath)
cv2.imshow("read",img)
cv2.waitkey(0)
cv2.imwrite("write.jpg",img)
