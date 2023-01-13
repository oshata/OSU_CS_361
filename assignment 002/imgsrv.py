
import os
import time
NUM_IMAGES = len(os.listdir('./images'))


def img_service():
    print('imgsrv.py running...')
    while True:
        time.sleep(1.0)
        with open("image-service.txt", "r+") as file:
            line = file.readline().strip()
            if line.isdigit():
                num = int(line)
                num = num % NUM_IMAGES
                file.seek(0)
                file.write(f"/images/{num}.jpg")
                file.truncate()


if __name__ == '__main__':
    img_service()
