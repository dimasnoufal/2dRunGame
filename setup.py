import pygame

# Define Constant Variable
# Window Size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Setting Image and Text (Size, Path)
# function for drawing text on the screen
def draw_text(text, font_name, size, text_color, position_x, position_y, position):
    font = pygame.font.Font(font_name, size)  # loads font

    text_plane = font.render(text, True, text_color)  # renders given text in the selected font
    text_rect = text_plane.get_rect()

    # setting text position
    if position == "midtop":
        text_rect.midtop = (int(position_x), int(position_y))
    elif position == "topright":
        text_rect.topright = (int(position_x), int(position_y))

    SCREEN.blit(text_plane, text_rect)  # draws the rendered text on the screen


# function for loading single image file
def load_image(path, size_x=0, size_y=0):
    image = pygame.image.load(path).convert_alpha()  # loads image file and converts it into pixels

    if size_x > 0 and size_y > 0:
        image = pygame.transform.scale(image, (size_x, size_y))  # resizing the image to the given size

    return image, image.get_rect()


# function for loading multiple image files in a list
def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
    images = []  # declaring list to store the images

    for i in range(0, number_of_image):

        path = image_path + image_name_prefix + str(i) + ".png"  # creating the path string
        image = pygame.image.load(path).convert_alpha()  # loads image file and converts it into pixels

        if size_x > 0 and size_y > 0:
            image = pygame.transform.scale(image, (size_x, size_y))  # resizing the image to the given size

        images.append(image)

    return images


# Image Character (Dino)
RUNNING = load_sprites("image/character/cat/", "run_", 8, 190, 153)

JUMPING = load_sprites("image/character/cat/", "jump_", 15, 190, 153)

DUCKING = load_sprites("image/character/cat/", "slide_", 10, 190, 153)

# Image Obstacle

CACTUS_1 = load_sprites("image/obstacle/cactus/", "cactus1_", 2, 160, 160)

CACTUS_2 = load_sprites("image/obstacle/cactus/", "cactus2_", 2, 160, 185)

BIRD = load_sprites("image/obstacle/bird/", "bird_", 2, 120, 120)

# Sound
JUMP_SOUND = pygame.mixer.Sound("sound/Jump.ogg")

SCORE_SOUND = pygame.mixer.Sound("sound/score.ogg")

GAME_OVER_SOUND = pygame.mixer.Sound("sound/game_over.ogg")

MENU_SOUND = pygame.mixer.Sound("sound/menu.ogg")

# Font
font = pygame.font.Font('freesansbold.ttf', 20)
