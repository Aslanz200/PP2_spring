import pygame , sys , random
pygame.init()


#setting the display
SCREEN_WIDTH , SCREEN_LENGTH = 600 , 600
screen = pygame.display.set_mode((SCREEN_LENGTH , SCREEN_WIDTH))
FPS = pygame.time.Clock()
BLOCK_SIZE = 30  #block size
speed = 5   #speed of snake
score = 0   #our score


#creating a text for score
Font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial Black.ttf" , 50)
score_txt = Font.render("0" , True , "White")
score_rect = score_txt.get_rect(center=(SCREEN_LENGTH/2 , SCREEN_WIDTH/2))



#creating a squared grid
def DrawGrid():
    for x in range (0 , SCREEN_LENGTH , BLOCK_SIZE):
        for y in range(0 , SCREEN_WIDTH , BLOCK_SIZE):
            rect = pygame.Rect(x , y , BLOCK_SIZE , BLOCK_SIZE)
            pygame.draw.rect(screen , "#3c3c3b" , rect , 1)



#snake class
class Snake:
    def __init__(self):
        self.x , self.y = BLOCK_SIZE , BLOCK_SIZE
        self.xdir = 1   #xdir 
        self.ydir = 0 
        self.head = pygame.Rect(self.x , self.y , BLOCK_SIZE , BLOCK_SIZE)   #snake head
        self.body = [pygame.Rect(self.x-BLOCK_SIZE , self.y , BLOCK_SIZE , BLOCK_SIZE)]   #snake body
        self.dead = False
    def update(self):

        global apple    
        global speed
        global score

        if self.dead:
            self.x , self.y = BLOCK_SIZE , BLOCK_SIZE
            self.head = pygame.Rect(self.x , self.y , BLOCK_SIZE , BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE , self.y , BLOCK_SIZE , BLOCK_SIZE)]
            self.xdir = 1      
            self.ydir = 0
            self.dead = False
            apple = Apple()
            speed = 5
            score = 0

        #collision 
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0 , SCREEN_LENGTH) or self.head.y not in range(0, SCREEN_WIDTH):
                self.dead = True

        #snake moving
        self.body.append(self.head)  #appending a block ahead of body so there will be no off-range errors
        for i in range(len(self.body)-1):  
            self.body[i].x , self.body[i].y = self.body[i+1].x , self.body[i+1].y   #moving each body block forward
        self.head.x += self.xdir * BLOCK_SIZE      #moving head by moving its position by one block
        self.head.y += self.ydir * BLOCK_SIZE      
        self.body.remove(self.head)



class Apple:
    def __init__(self):
        self.x = int(random.randint(0 , SCREEN_LENGTH)/BLOCK_SIZE) * BLOCK_SIZE  #landing apples right on grid
        self.y = int(random.randint(0, SCREEN_WIDTH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x , self.y , BLOCK_SIZE , BLOCK_SIZE)  #apple size
    def update(self):
        pygame.draw.rect(screen , "Red" , self.rect)    #appending on the screen


DrawGrid()
snake = Snake()
apple = Apple()

count = 0
on = True
while on:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
            sys.exit()
        if event.type == pygame.KEYDOWN:        #movement of the snake depending on the key clicked
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            if event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            if event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
            if event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1


    snake.update()
    screen.fill("Black")
    DrawGrid()
    apple.update()

    score_txt = Font.render(f"{score}" , True , "White")

    pygame.draw.rect(screen , 'Yellow' , snake.head)
    screen.blit(score_txt , score_rect)
    for square in snake.body:
        pygame.draw.rect(screen , "Green" , square)
    pygame.display.update()

    if snake.head.x == apple.x and snake.head.y == apple.y:     #appending new block to the snake depending on the collision with apple
        snake.body.append(pygame.Rect(square.x , square.y , BLOCK_SIZE , BLOCK_SIZE))
        apple = Apple()
        score += 1
        speed += 0.1
    FPS.tick(speed)
pygame.quit()