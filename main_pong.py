import random
import pygame

pygame.init()

# Colors and RGB tuple...
white = (255, 255, 255)
black = (0, 0, 0)
red = (253, 76, 76)
orange = (255, 127, 80)
violet = (75, 0, 130)
blue = (0, 0, 255)

# Game Variables
run = True
game_over = True
s_width = int(800)
s_height = int(600)
fps = 30
clock = pygame.time.Clock()
pad_speed = 5
ball_speed = 1.5
b_speed = [ball_speed, -ball_speed]  # This list to choose a random direction when the game begins.
global bspd_x, bspd_y
bspd_x = int(random.choice(b_speed))
bspd_y = int(random.choice(b_speed))
temp = False

# Object measurements
pad_ht = 70
pad_wh = 20
ball_rd = 10
radius = 15
global ball_x, ball_y
ball_x = int(s_width / 2)
ball_y = int(s_height / 2)

# Window
window = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Pong Game")
pygame.display.update()


class Bar(object):
    def __init__(self, x, y, x_size, y_size):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        Bar.draw(self)

    def draw(self):
        pygame.draw.rect(window, red, (self.x, self.y, self.x_size, self.y_size))

    def move(self, newY):
        self.y += newY
        if self.y < 0:
            self.y = 0
        elif (self.y + pad_ht) > s_height:
            self.y = s_height - pad_ht
        self.draw()


# Method to move the ball
def b_move(b_x, b_y, bs_x, bs_y, gover, t):
    b_x += bs_x
    b_y += bs_y
    # Collision handling for walls
    if b_y + radius > s_height or b_y - radius < 0:  # If the ball hits the TOP or BOTTOM SIDE of the screen
        bs_y *= -1
    if b_x + radius + 2 > s_width or b_x - radius - 2 < 0:  # If the ball hits the RIGHT or LEFT SIDE of the screen
        gover = True
        t = True
    return b_x, b_y, bs_x, bs_y, gover, t


# Method to display text in game window
def text_screen(text, color, size, x, y):
    pygame.font.init()
    font = pygame.font.SysFont('constantia', size)
    text_on_screen = font.render(text, True, color)
    window.blit(text_on_screen, (x, y))


print(pygame.font.get_fonts())

# Declaring RIGHT and LEFT BARS along with BALL
b_left = Bar((s_width / 10 - 20), (s_height / 2 - 35), pad_wh, pad_ht)
b_right = Bar((s_width - 80), (s_height / 2 - 35), pad_wh, pad_ht)
ball = pygame.draw.circle(window, black, (ball_x, ball_y), radius)

# Game Loop
while run:
    # Game initialization
    Player1 = 0  # Player-1 score
    Player1_c = 0
    Player2 = 0  # Player-2 score
    Player2_c = 0
    ball_x = int(s_width / 2)
    ball_y = int(s_height / 2)
    bspd_x = int(random.choice(b_speed))
    bspd_y = int(random.choice(b_speed))

    # Actual game functioning
    window.fill(white)
    window.fill(orange, (0, s_height / 3, s_width, s_height / 3))
    text_screen(" -- PONG -- ", violet, 80, s_width / 3 - 64, s_height / 4 + 5)
    text_screen("Click any key to play PONG", black, 30, s_width / 3 - 32, s_height / 2.1)
    pygame.display.update()
    for click in pygame.event.get():
        if click.type == pygame.QUIT:
            run = False
        if click.type == pygame.KEYDOWN:
            game_over = False
    while not game_over:
        window.fill(white)
        Bar.draw(b_left)
        Bar.draw(b_right)
        pygame.draw.lines(window, red, True, [(s_width / 2 - 2, 30), (s_width / 2 - 2, 570)], 2)
        pygame.draw.circle(window, black, (ball_x, ball_y), radius)
        ball_x, ball_y, bspd_x, bspd_y, game_over, temp = b_move(ball_x, ball_y, bspd_x, bspd_y, game_over,
                                                                 temp)  # Collision handling for walls

        text_screen("- Score -", black, 40, s_width / 2 - 77, 0)
        text_screen(str(Player1), black, 70, s_width / 3, 40)
        text_screen(str(Player2), black, 70, (s_width - s_width / 2.5), 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            b_right.move(- pad_speed)
        if keys[pygame.K_DOWN]:
            b_right.move(pad_speed)
        if keys[pygame.K_w]:
            b_left.move(- pad_speed)
        if keys[pygame.K_s]:
            b_left.move(pad_speed)

        # Collision handling for pads or bars
        for i in range(int(b_right.y), int(b_right.y + b_right.y_size)):
            if abs(i - ball_y) <= (radius + 3):
                print(b_right.y, b_right.y + b_right.y_size, abs(b_right.y - ball_y),
                      (b_right.y + b_right.y_size) - ball_y)
                # print("  ...x check")
                if abs(abs(b_right.x + (b_right.x + b_right.x_size)) / 2 - ball_x) <= (radius + 4):
                    print(b_right.x, b_right.x + b_right.x_size, abs(b_right.x - (b_right.x + b_right.x_size) / 2),
                          abs(abs(b_right.x - (b_right.x + b_right.x_size) / 2) - ball_x))
                    bspd_x *= -1
                    Player2_c += 1
        for i in range(int(b_left.y), int(b_left.y + b_left.y_size)):
            if abs(i - ball_y) <= (radius + 3):
                if abs(abs(b_left.x + (b_left.x + b_left.x_size)) / 2 - ball_x) <= (radius + 4):
                    bspd_x *= -1
                    Player1_c += 1
        if Player1_c != 0:
            Player1 += 5
            Player1_c = 0
        elif Player2_c != 0:
            Player2 += 5
            Player2_c = 0
        pygame.display.update()

    # Final WINDOW after the GAME is OVER
    if Player1 > Player2:
        while temp:
            window.fill(white)
            text_screen(" Congratulations, Player-1 WON", blue, 50, s_width / 2 - 350, s_height / 2 - 100)
            text_screen("Player-1 : " + str(Player1), violet, 40, s_width / 2 - 80, s_height / 2)
            text_screen("Player-2 : " + str(Player2), violet, 40, s_width / 2 - 80, s_height / 2 + 40)
            text_screen("Press  'Enter' to Play Again  or  'Esc' to Exit", red, 20, s_width / 2 - 170,
                        s_height / 2 + 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    temp = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        temp = False
                        run = False
                    if event.key == pygame.K_RETURN:
                        temp = False
    elif Player2 > Player1:
        while temp:
            window.fill(white)
            text_screen(" Congratulations, Player-2 WON", blue, 50, s_width / 2 - 350, s_height / 2 - 100)
            text_screen("Player-2 : " + str(Player2), violet, 40, s_width / 2 - 80, s_height / 2)
            text_screen("Player-1 : " + str(Player1), violet, 40, s_width / 2 - 80, s_height / 2 + 40)
            text_screen("Press  'Enter' to Play Again  or  'Esc' to Exit", red, 20, s_width / 2 - 170,
                        s_height / 2 + 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    temp = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        temp = False
                        run = False
                    if event.key == pygame.K_RETURN:
                        temp = False
    else:
        while temp:
            window.fill(white)
            text_screen(" DRAW", blue, 60, s_width / 2 - 100, s_height / 2 - 100)
            text_screen("Player-1 : " + str(Player1), violet, 40, s_width / 2 - 80, s_height / 2)
            text_screen("Player-2 : " + str(Player2), violet, 40, s_width / 2 - 80, s_height / 2 + 40)
            text_screen("Press  'Enter' to Play Again  or  'Esc' to Exit", red, 20, s_width / 2 - 170,
                        s_height / 2 + 200)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    temp = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        temp = False
                        run = False
                    if event.key == pygame.K_RETURN:
                        temp = False
    # Handling time
    pygame.time.delay(30)
    clock.tick(fps)
pygame.quit()
quit()
