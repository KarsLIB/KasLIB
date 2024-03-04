import cv2
class faceshot():
    def faceShotMain():
        names = input("WTF do ya want to TAKE a shot? : ")
        ##path = "{}".format(names)
        ##os.mkdir(path)
        video = cv2.VideoCapture(0)
        imagecounter = 0
        while True:
            ret, frame = video.read()
            if not ret:
                print("error!")
                break
            cv2.imshow("katshotig", frame)
            wait_key = cv2.waitKey()
            if wait_key%256 == 27:
                print("Escape hit, closing...")
                break
            elif wait_key%256 == 32:
                img_name = "dataset/"+ names +"/image_{}.jpg".format(imagecounter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                imagecounter += 1
        video.release()
        cv2.destroyAllWindows()
                
