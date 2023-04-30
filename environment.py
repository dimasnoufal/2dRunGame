from setup import *


class Background:
    def __init__(self, image_path, speed=10):
        self.image0, self.rect0 = load_image(image_path, 1280, 720)
        self.image1, self.rect1 = load_image(image_path, 1280, 720)

        self.rect0.bottom = SCREEN_HEIGHT
        self.rect1.bottom = SCREEN_HEIGHT

        self.rect1.left = self.rect0.right

        self.speed = speed

    def update(self):
        self.rect0.left -= int(self.speed)
        self.rect1.left -= int(self.speed)

        if self.rect0.right < 0:
            self.rect0.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect0.right

    def draw(self):
        SCREEN.blit(self.image0, self.rect0)
        SCREEN.blit(self.image1, self.rect1)


class AllBackgrounds:
    def __init__(self, game_speed):
        self.backgroud_0 = Background("image/background/bg_0.png", game_speed)
        self.backgroud_1 = Background("image/background/bg_1.png", game_speed - 12)
        self.backgroud_2 = Background("image/background/bg_2.png", game_speed - 13)
        self.backgroud_3 = Background("image/background/bg_3.png", game_speed - 14)

    def update_speed(self, speed):
        self.backgroud_0.speed = speed
        self.backgroud_1.speed = speed - 12
        self.backgroud_2.speed = speed - 13
        self.backgroud_3.speed = speed - 14

    def draw(self):
        self.backgroud_3.draw()
        self.backgroud_2.draw()
        self.backgroud_1.draw()
        self.backgroud_0.draw()

    def update(self):
        self.backgroud_3.update()
        self.backgroud_2.update()
        self.backgroud_1.update()
        self.backgroud_0.update()
