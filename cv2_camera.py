
import cv2
import time

class Camera:
    def __init__(self, img = None):
        self.img = img
        self.index = 0
        self.time = int(time.time()*1000)
        self.color_modes = ["BGR", "GRAY", "NORMAL"]
        self.mode = None

    def set_color_mode(self, index_mode):
        if index_mode > len(self.color_modes):
            return
        self.mode = self.color_modes[index_mode]

    def print(self):
        print(self.mode)

    def save_file(self):
        cv2.imwrite(f'./img/img_{self.time}.jpeg', self.img)

    def camera_frames(self):
        cap = cv2.VideoCapture(self.index)
        while True:
            _, self.img = cap.read()
            self.img = cv2.flip(self.img, 1)
            if self.mode == 'BGR':
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            elif self.mode == 'GRAY':
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('camera', self.img)
            if cv2.waitKey(10) == 27:
                self.save_file()
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    cm = Camera()
    cm.set_color_mode(1)  # method for adjusting the color mode
    cm.print()
    cm.camera_frames()
