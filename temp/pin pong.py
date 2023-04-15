from pygame import *


font.init()
font = font.Font(None, 40)
win = font.render('you win', True, (255,215,0))
lose = font.render('you lose', True, (255,0,0))
win_width = 700
win_height = 500
speed = 5

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
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_d] and self.rect.x < 600:
            self.rect.x += self.speed

        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed



window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')



rock = Player('rocket.png', 350, 430, 65, 65, speed)

monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()


for i in range (1, 6):
    monster = Enemy('ufo.png', randint(5, 615), -50, 80, 50, randint(1, 2))
    monsters.add(monster)

for i in range (1,4):
    asteroid = Enemy('asteroid.png', randint(5, 615), -50, 65, 65, randint(1, 2))
    asteroids.add(asteroid)

background = transform.scale(image.load('almazi.jpg'),(700, 500))
FPS = 60
clock = time.Clock()
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rock.fire()

    if not finish:
        window.blit(background, (0,0))
        rock.update()

        
    display.update()
    clock.tick(FPS)