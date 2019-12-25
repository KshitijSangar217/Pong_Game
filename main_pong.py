import pygame

pygame.init()

#Colors and RGB tuple...
white = (255, 255, 255)
black = (0, 0, 0)
red = (253, 76, 76)
orange = (255, 127, 80)
violet = (75,0,130)

#Game Variables
run = True
game_over = True #False <-- previous
s_width = 800
s_height = 600
fps = 30
clock = pygame.time.Clock()
pad_speed = 0.5
ball_speed = 10

pad_ht = 70
pad_wh = 20
ball_rd = 20

#Window
window = pygame.display.set_mode((s_width,s_height))
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
    def move(self,newY):
        self.y += newY
        self.draw()

#Method to display text in game window
def text_screen(text, color, size, x, y):
    pygame.font.init()
    font = pygame.font.SysFont('constantia', size)
    text_on_screen = font.render(text, True, color)
    window.blit(text_on_screen, (x,y))
print(pygame.font.get_fonts())

#Declaring RIGHT and LEFT BARS
b_left  = Bar((s_width/10 - 20), (s_height/2 - 35), pad_wh, pad_ht)
b_right = Bar((s_width -80), (s_height/2 - 35), pad_wh, pad_ht)

#Game Loop
while(run):
    Player1 = 0  # Player-1 score
    Player2 = 0  # Player-2 score
    window.fill(white)
    window.fill(orange,(0, s_height/3, s_width, s_height/3))
    text_screen(" -- PONG -- ", violet, 80, s_width / 3 - 64, s_height / 4 + 5)
    text_screen("Click any key to play PONG", black, 30, s_width/3 - 32, s_height/2.1)
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
        pygame.draw.lines(window, red, True, [(s_width/2 - 10, 30), (s_width/2 - 10, 570)], 2)
        text_screen("- Score -", black, 40, s_width/2-77, 0)
        text_screen(str(Player1), black, 70, s_width/3, 40)
        text_screen(str(Player2), black, 70, (s_width - s_width/2.5), 40)

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


        pygame.display.update()

    #Handling time
    pygame.time.delay(30)
    clock.tick(fps)

pygame.quit()
quit()


