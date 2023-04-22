from pygame import *


font.init()
font = font.Font(None, 40)
lose1 = font.render('игрок 1 проиграл(((', True, (255,0,0))
lose2 = font.render('игрок 2 проиграл(((', True, (255,0,0))
win_width = 700
win_height = 500
speed = 5
speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_width
        self.height = player_height      
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_s] and self.rect.y < 370:
            self.rect.y += self.speed

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed


window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')



rock1 = Player('platform.png', 2, 300, 65, 120, speed)
rock2 = Player('platform.png', 640, 300, 65, 120, speed)
ball = GameSprite('ball.png', 350, 430, 65, 65, speed)




background = transform.scale(image.load('blue.jpg'),(700, 500))
FPS = 60
clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        


    if not finish:
        window.blit(background, (0,0))
        rock1.update_l()
        rock2.update_r()
        ball.reset()
        rock1.reset()
        rock2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(rock1, ball) or sprite.collide_rect(rock2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1,(200,200))

    if ball.rect.x > 650:
        finish = True
        window.blit(lose2,(200,200))

    display.update()
    clock.tick(FPS)