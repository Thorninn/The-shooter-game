#Create your own shooter
from pygame import *
from spriteclass import GameSprite, Player
from random import randint

lose = 0
class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y > 500:
            self.rect.x = randint(5, 700-70)
            self.rect.y = 0
            lose += 1 

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('The Shooter Game')
clock = time.Clock()
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height) )

player = Player(player_image='rocket.png',
                    player_x=300, player_y=500-70,
                    width=65, height=65, player_speed=5)

monster_group = sprite.Group()
for i in range(1,6):
    monster = Enemy(player_image='ufo.png',
                    player_x=randint(5, 700-70),
                    player_y =50,
                    width=65, height=65,
                    player_speed=randint(1,3))
    monster_group.add(monster)

font.init()
style = font.Font(None, 30)

score = 0
lose = 0
win = False
finish = True
run = True

while run:

    if finish:
        window.blit(background, (0,0))
        player.reset(window)
        player.update()
        monster_group.draw(window)
        monster_group.update()

        player.bullet_group.draw(window)
        player.bullet_group.update()

        collides = sprite.groupcollide(monster_group, player.bullet_group, True, True)

        for col in collides:
            score += 1
            new_monster = Enemy(player_image='ufo.png',
                            player_x=randint(5, 700-70),
                            player_y=50,
                            width=65, height=65,
                            player_speed=randint(1, 3))
            monster_group.add(new_monster)

        if score >= 10:
            finish = False
            win = True

        collides_2 = sprite.spritecollide(player, monster_group, False)

        for col2 in collides_2:
                finish = False

        
        missing = style.render('Missed: ' + str(lose), 1, (255, 255, 255))
        scoring = style.render('Score:' + str(score), 1, (255, 255, 255))
        window.blit(missing, (5, 5))
        window.blit(scoring, (5, 40))

        display.update()
        clock.tick(60)
    else:
        window.blit(background, (0, 0))
        if win:
            win_text = style.render('YOU WIN!', True, (0, 255, 0))
            window.blit(win_text, (250, 200))
        else:
            lose_text = style.render('YOU LOSE!', True, (255, 0, 0))
            window.blit(lose_text, (250, 200))
        display.update()
        time.delay(3000)

        # Reset the game state after showing message:
        for bullet in player.bullet_group:
            bullet.kill()
        for m in monster_group:
            m.kill()

        player.rect.x = 300
        player.rect.y = win_height - 70

        for i in range(5):
            monster = Enemy(player_image='ufo.png',
                            player_x=randint(5, 700-70),
                            player_y=50,
                            width=65, height=65,
                            player_speed=randint(1, 3))
            monster_group.add(monster)

        lose = 0
        score = 0
        win = False  # reset win flag
        finish = True
        
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()


    

