import cv2 

def camera_check():
    vid = cv2.VideoCapture(0)

    while(True):
        ret, frame = vid.read()
        if not ret:
            print(f'Failed to grab frame')
            break
        
        cv2.imshow('Camera Testing', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_check()