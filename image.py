import cv2      
import os        

folder = "images"

for i in os.listdir(folder):
    if i.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(folder, i)
        img = cv2.imread(path)

        cv2.imshow("slaid", img)
        cv2.waitKey(2000)


cv2.destroyAllWindows()
