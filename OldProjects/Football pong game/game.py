import pygame
from random import randint
from time import sleep

CurrentScore1 = 0
CurrentScore2 = 0
time = 0

class timePlaying(pygame.sprite.Sprite):
    def __init__(self):
        Timer = "0"
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 12)
        self.textSurf = self.font.render(Timer, 1, "white")
        self.image = pygame.Surface((20, 10))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center=(10,5))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [10/2 - W/2, 5/2 - H/2])

    def update(self, time):
        Timer = str(time)
        self.font = pygame.font.SysFont("Arial", 12)
        self.textSurf = self.font.render(Timer, 1, "white")
        self.image = pygame.Surface((20, 10))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center=(10,5))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [10/2 - W/2, 5/2 - H/2])
    
class Scoreboard1(pygame.sprite.Sprite):
    def __init__(self, size, color, width, height, locationY):
        CurrentScore1 = 0
        score = "Score: "+str(CurrentScore1)
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(score, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center=(400,locationY))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, CurrentScore1, size, color, width, height):
        CurrentScore1 += 1
        text1 = "Score: "+str(CurrentScore1)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text1, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        return CurrentScore1

class Scoreboard2(pygame.sprite.Sprite):
    def __init__(self, size, color, width, height, locationY):
        CurrentScore2 = 0
        score = "Score: "+str(CurrentScore2)
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(score, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center=(400,locationY))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

    def update(self, CurrentScore2, size, color, width, height):
        CurrentScore2 += 1
        text1 = "Score: "+str(CurrentScore2)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text1, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        return CurrentScore2

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((20, 50))
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 500:
          self.rect.y = 500

class Goal(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((50, 61))
        self.surf.fill((255,255,255))
        self.image = pygame.image.load(image_file)
        self.rect = self.surf.get_rect(center=(location))

class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255,255,255))
        self.image = pygame.image.load(image_file)
        self.rect = self.surf.get_rect(center=(400,250,))
        self.velocity = [randint(4,8),randint(-8,8)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def reset(self):
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(400,250,))
        self.velocity = [randint(4,8),randint(-8,8)]
                                       
pygame.init()

win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pong: Football edition")

clock = pygame.time.Clock()

scoreBoard1 = Scoreboard1(12,"white",100,50,25)
scoreBoard2 = Scoreboard2(12,"white",100,50,75)
timing = timePlaying()

player1 = Player(location =(50, 200))
player2 = Player(location =(720, 200))

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
goals = pygame.sprite.Group()

BackGround = Background('pitch.jpg', [0,0])
ball = Ball('football.png')
goal1 = Goal('goal.jpg', [25,250])
goal2 = Goal('goal2.jpg', [775,250])

all_sprites.add(scoreBoard1)
all_sprites.add(scoreBoard2)
all_sprites.add(timing)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)
all_sprites.add(BackGround)
players.add(player1)
players.add(player2)
goals.add(goal1)
goals.add(goal2)

run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.set_timer(event, 1000)
            time += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.moveUp(5)
    if keys[pygame.K_s]:
        player1.moveDown(5)
    if keys[pygame.K_UP]:
        player2.moveUp(5)
    if keys[pygame.K_DOWN]:
        player2.moveDown(5)

    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.spritecollideany(ball, players):
      ball.bounce()
    
    win.fill((0,0,0))
    win.blit(BackGround.image, BackGround.rect)
    pygame.draw.rect(win, (255, 255, 255), player1)
    pygame.draw.rect(win, (255, 255, 255), player2)
    win.blit(ball.image, ball.rect)
    win.blit(goal1.image, goal1.rect)
    win.blit(goal2.image, goal2.rect)
    win.blit(scoreBoard1.image,scoreBoard1)
    win.blit(scoreBoard2.image,scoreBoard2)
    win.blit(timing.image, timing)
    timing.update(time)
    ball.update()
    pygame.display.update()


    if pygame.sprite.spritecollideany(ball, players):
        ball.update()

    goal_scored = pygame.sprite.spritecollideany(ball, goals)

    if goal_scored == goal2:
        ball.kill()
        sleep(1)
        CurrentScore1 = scoreBoard1.update(CurrentScore1,12,"white",100,50)
        ball.reset()

    if goal_scored == goal1:
        ball.kill()
        sleep(1)
        CurrentScore2 = scoreBoard2.update(CurrentScore2,12,"white",100,50)
        ball.reset()

pygame.quit()

