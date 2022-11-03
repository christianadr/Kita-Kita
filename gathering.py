import os
import time
import uuid
import cv2

PARENT_PATH = os.getcwd() # Get parent directory

# Function to check whether the given path exists
def dir_exists(path):
    
    if not os.path.exists(os.path.join(PARENT_PATH, path)):
        return False
    
    else:
        return True
    
# Function to create non-existing path
def create_dir(path):
    
    # If directory does not exists, create the given directory,
    # else console print 'Directory already exists.'.
    if (dir_exists(path) == False):
        os.makedirs(os.path.join(PARENT_PATH, path))
    
    else:
        print('Directory already exists.')
        
# Function to collect images from webcam
def collect_images(images_num, path):
    
    cap = cv2.VideoCapture(0)
    
    for num in range(images_num):
        print(f'Collecting image {num + 1} ... ', end = '\r')
        ret, frame = cap.read()
        img_name = os.path.join(path, f'{str(uuid.uuid1())}.jpg') # Assigning random name for each image
        cv2.imwrite(img_name, frame)
        cv2.imswhow('Collecting images', frame)
        time.sleep(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    print(f'Done collecting images', end = '\r')
    
if __name__ == '__main__':
    print(f'running gathering.py ...' end = '\r')
    IMAGE_PATH = os.path.join('data', 'images')
    create_dir(IMAGE_PATH)
    collect_images(30, IMAGE_PATH)
    

        