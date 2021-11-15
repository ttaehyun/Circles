
# game options/settings
TITLE = "TEST"
WIDTH = 1280
HEIGHT = 720
FPS = 60
FONT_NAME = 'arial'

# Player properties
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH/2 - 50, HEIGHT*3/4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (300, 200, 100, 20),
                 (175, 100, 65, 20),
                 (1000, 400, 80, 20),
                 (400, 300, 100, 20),
                 (800, 350, 150, 20),
                 (1200, 30, 200, 20),
                 ]



# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE