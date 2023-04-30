from pygame import *
from random import randint
 
 
window = display.set_mode((700,500))
display.set_caption('cago')
 
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 100)
lost = 0
kill = 0
live = 3
 
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
 
clock = time.Clock()
FPS = 120
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        if key_pressed[K_d] and self.rect.x <=600:
            self.rect.x += self.speed
        if key_pressed[K_a] and self.rect.x >=5:
            self.rect.x -= self.speed
    def update(self):
        global lost
        global kill 
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(30,605)
            self.speed = randint(1,5)
            lost += 1
        grcoll = sprite.groupcollide(bullets, UFO, True, True)
        for el in grcoll:
            kill +=1
            ufo6 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
            UFO.add(ufo6)
 
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top ,15, 20, 5)
        bullets.add(bullet)
 
class Bullet(GameSprite):
    def update(self):
        global kill
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        grcoll = sprite.groupcollide(bullets, UFO, True, True)
        for el in grcoll:
            kill += 1
            ufo6 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
            UFO.add(ufo6)
 
class Asteroid(GameSprite):
    def update(self):
        global live
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(30,605)
            self.speed = randint(1,5)
        grcoll1 = sprite.groupcollide(bullets, asteroids, True, False)
        grcoll2 = sprite.spritecollide(rocket, asteroids,True)
        for el in grcoll2:
            live -=1
            asteroid4 = Asteroid('asteroid.png',randint(30,605), 0 , 70, 70, 3)
            asteroids.add(asteroid4)
 
 
 
 
 
 
 
rocket = GameSprite('rocket.png', 650, 450, 100, 100,7.9)
ufo1 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
ufo2 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
ufo3= GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
ufo4 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
ufo5 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
asteroid1 = Asteroid('asteroid.png',randint(30,605), 0 , 70, 70, 3)
asteroid2 = Asteroid('asteroid.png',randint(30,605), 0 , 70, 70, 3)
asteroid3 = Asteroid('asteroid.png',randint(30,605), 0 , 70, 70, 3)
bagr = transform.scale(image.load('galaxy.jpg'),(700,500))
heart1 = GameSprite('bullet.png',0, 72 , 24, 36, 0)
heart2 = GameSprite('bullet.png',24, 72 , 24, 36, 0)
heart3 = GameSprite('bullet.png',48 ,72 , 24, 36, 0)
 
 
bullets = sprite.Group()
 
asteroids = sprite.Group()
asteroids.add(asteroid1,asteroid2,asteroid3)
 
UFO = sprite.Group()
UFO.add(ufo1,ufo2, ufo3, ufo4, ufo5)
 
game = True
finish = True
 
while game:
    key_pressed = key.get_pressed()
    for i in event.get():
 
        if i.type == QUIT:
            game = False
        elif key_pressed[K_SPACE]:
            rocket.fire()
    if finish == True:
 
        window.blit(bagr , (0,0))
        text_lose1 = font1.render('Пропущено: ' + str(lost), 1, (255,255,255))
        text_lose2 = font1.render('Убиты: ' + str(kill), 1, (255,255,255))
        window.blit(text_lose1, (0, 0))
        window.blit(text_lose2, (0, 36))
        rocket.reset()
        bullets.draw(window)
        bullets.update()
        UFO.draw(window)
        UFO.update()
        asteroids.draw(window)
        asteroids.update()
 
        if live == 3:
            heart1.reset()
            heart2.reset()
            heart3.reset()
 
        elif live == 2:
            heart1.reset()
            heart2.reset()
 
        elif live == 1:
            heart1.reset()
 
        elif live == 0:
            text_lose3 = font2.render('YOU LOSE' , 1, (255,255,255))
            window.blit(text_lose3, (250, 250))
            finish = False
 
        if kill >= 26:
            text_lose3 = font2.render('YOU WIN' , 1, (255,255,255))
            window.blit(text_lose3, (250, 250))
            finish = False
        if lost >= 26:
            text_lose4 = font2.render('YOU LOSE' , 1, (255,255,255))
            window.blit(text_lose4, (250, 250))
            finish = False
 
 
        rocket.move()
 
    clock.tick(FPS)
    display.update() 
















































































































































































"""000000000000000000000000000000000000000000000000000000
   000000000000001111114000000000000011111140000000000000
   000000000011111111111111000000111111111111110000000000
   000000005111111111111111110051111111111111111100000000
   000000011111111111111111111111111111111111111110000000
   000000111111111110000001111111140000051111111111000000
   000005111111114000000000051110000000000011111111100000
   000001111111140000000000000400000000000001111111100000
   000001111111000000000000000000000000000000111111110000
   000001111111000000000000000000000000000000111111110000
   000001111111000000000000000000000000000000111111150000
   000001111111000000000000000000000000000000111111100000
   000005111111100000000000000000000000000001111111100000
   000000111111110000000000000000000000000011111111000000
   000000011111111100000000000000000000005111111110000000
   000000001111111111500000000000000004111111111100000000
   000000000011111111111100000000005111111111114000000000
   000000000004111111111111000000511111111111500000000000
   000000000000004111111111140001111111111500000000000000
   000000000000000001111111110011111111100000000000000000
   000000000000000000051111111111111110000000000000000000
   000000000000000000000111111111111000000000000000000000
   000000000000000000000041111111150000000000000000000000
   000000000000000000000000111111500000000000000000000000
   000000000000000000000000011111000000000000000000000000
   000000000000000000000000051110000000000000000000000000
   000000000000000000000000001100000000000000000000000000
   000000000000000000000000000400000000000000000000000000
   000000000000000000000000000000000000000000000000000000"""