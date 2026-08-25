import cv2
import numpy as np
        
h, w = (200, 280)

arr: np.ndarray = np.full((200, 280, 3), 255, dtype=np.uint8)

I, J = np.ogrid[:h, :w]
cond = ((I%60<30) & (J%60 < 30) | (I%60>=30) & (J%60>=30))

arr[cond, :] = (0, 0, 0)

cv2.imwrite("img/vectortest.jpg", arr)

