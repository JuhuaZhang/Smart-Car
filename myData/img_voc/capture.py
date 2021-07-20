import cv2

for i in range(0,1000):
    cap = cv2.VideoCapture(0)
    flag = cap.isOpened()

    if flag:
        ret,frame = cap.read()
        cv2.imshow("Capture", frame)
        cv2.waitKey()
        if i < 10
            cv2.imwrite("./"+ "00000" + str(i)+ ".jpg", frame)
        elif i<100
            cv2.imwrite("./"+ "0000" + str(i)+ ".jpg", frame)
        else:
            cv2.imwrite("./"+ "000" + str(i)+ ".jpg", frame)
        print("save " + str(i) +"th image successfully!")
        cap.release()
        cv2.destroyAllWindows()
        
    
