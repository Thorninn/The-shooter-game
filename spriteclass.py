from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, 
                 width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.missed_score = 0


        self.bullet_group = sprite.Group()

    # methods
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y) )


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <= 700-70:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(player_image='bullet.png',
                        player_x=self.rect.centerx,
                        player_y=self.rect.top,
                        width=15, height=20, player_speed=10)
        
        self.bullet_group.add(bullet)



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
    