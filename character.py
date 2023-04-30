from setup import *


class Character:
    X_POS = 80
    Y_POS = 490
    Y_POS_DUCK = 510
    JUMP_VEL = 12

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.character_duck = False
        self.character_run = True
        self.character_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.X_POS
        self.character_rect.y = self.Y_POS

    def update(self, userInput):
        if self.character_duck:
            self.duck()
        if self.character_run:
            self.run()
        if self.character_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.character_jump:
            JUMP_SOUND.play()
            self.character_duck = False
            self.character_run = False
            self.character_jump = True
        elif userInput[pygame.K_DOWN] and not self.character_jump:
            self.character_duck = True
            self.character_run = False
            self.character_jump = False
        elif not (self.character_jump or userInput[pygame.K_DOWN]):
            self.character_duck = False
            self.character_run = True
            self.character_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index % 10]
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.X_POS
        self.character_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        # pass

    def run(self):
        self.image = self.run_img[self.step_index % 8]
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.X_POS
        self.character_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.step_index % 15]
        if self.character_jump:
            self.character_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.character_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.character_rect.x, self.character_rect.y))
