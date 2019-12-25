import pygame

#Colors and RGB tuple...
white = (255, 255, 255)
black = (0, 0, 0)
red = (253,76,76 )

#Game Variables
run = True
game_over = False
s_width = 700
s_height = 600
fps = 30
clock = pygame.time.Clock()

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


#Declaring RIGHT and LEFT BARS
b_left = Bar(75,275,20,65)
b_right = Bar(600,275,20,65)

#Game Loop
while(run):
    window.fill(white)
    while not game_over:
        window.fill(white)
        Bar.draw(b_left)
        Bar.draw(b_right)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    b_right.move(-10)
                elif event.key == pygame.K_DOWN:
                    b_right.move(10)
                elif event.key == pygame.K_w:
                    b_left.move(-10)
                elif event.key == pygame.K_s:
                    b_left.move(10)


        #run, game_over = b_left.move(run, game_over)
        #run, game_over = b_right.move(run, game_over)

        pygame.display.update()

    #Handling time
    pygame.time.delay(30)
    clock.tick(fps)

pygame.quit()
quit()


