
import time


def ui_running():
    print('ui.py running...')
    while True:
        user_input = input("Enter 1 to generate new image or 2 to exit: ")
        if user_input == "1":
            with open("prng-service.txt", "w") as file:
                file.write("run")
            time.sleep(3)
            with open("prng-service.txt") as file:
                rand_num = int(file.readline())
            with open("image-service.txt", "w") as file:
                file.write(str(rand_num))
            time.sleep(3)
            with open("image-service.txt") as file:
                image_path = file.readline()
            print(image_path)
        elif user_input == "2":
            break
        else:
            print("Unknown option.")
            ui_running()


if __name__ == '__main__':
    ui_running()
