import pygame, math, sys, pygame.font
from pygame.locals import *
pygame.init()

class AvatarSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.transform.scale(pygame.image.load('penguin.png'), (50, 50))
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_up = self.k_down = 0
        self.rect = pygame.rect.Rect(self.position, self.image.get_size())

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y =y
    def update(self, dt):

        key_dict = pygame.key.get_pressed()
        if key_dict[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key_dict[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if key_dict[pygame.K_UP]:
            self.rect.y -= 300 * dt
        if key_dict[pygame.K_DOWN]:
            self.rect.y += 300 *dt

class MonsterSprite(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.transform.scale(pygame.image.load(image), (50, 50))
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_up = self.k_down = 0
        self.rect = pygame.rect.Rect(self.position, self.image.get_size())
        self.direction = direction
        # self.move = 9

    def update(self, inc, dt):

        if self.direction == "RIGHT":
            self.rect.x += inc * dt
            if self.rect.x + inc * dt >= 1024 - self.rect.width:
                self.direction = "LEFT"
        if self.direction == "LEFT":
            self.rect.x -= inc * dt
            if self.rect.x - inc * dt <= 0:
                self.direction = "RIGHT"

        if self.direction == "UP":
            self.rect.y += inc * dt
            if self.rect.y + inc * dt >= 500 - self.rect.width:
                self.direction = "DOWN"

        if self.direction == "DOWN":
            self.rect.y -= inc * dt
            if self.rect.y - inc * dt <= 0:
                self.direction = "UP"


class Game():

    def main(self, screen):
        pygame.init()

        clock = pygame.time.Clock()
        pygame.display.set_caption("World's easiest game!")

        rect = screen.get_rect()
        avatar = AvatarSprite('penguin.png', (900, 250))
        #
        avatar_group = pygame.sprite.RenderPlain(avatar)
        monsters = [MonsterSprite("monster.png", (100, 0), "UP"),
                MonsterSprite("monster.png", (250, 0), "UP"),
                MonsterSprite("monster.png", (400, 0), "UP"),
                MonsterSprite("monster.png", (550, 0), "UP"),
                MonsterSprite("monster.png", (700, 0), "UP"),
                MonsterSprite("monster.png", (850, 0), "UP"),
                    ]
        monster_group = pygame.sprite.RenderPlain(*monsters)

        # font = pygame.font.Font('freesansbold.ttf', 15)
        # screen.fill((0, 0, 0))
        # pygame.draw.line(screen, (0, 0, 0), (900, 0), (900, 500), 50)
        while 1:
            if avatar.rect.x <= 80:
                my_font = pygame.font.SysFont("monospace", 40)
                label = my_font.render("You Won!", 1, (0, 0, 0))
                screen.blit(label, (512, 250))

                pygame.quit()

            collisions = pygame.sprite.spritecollide(avatar, monster_group, False)
            print(collisions)

            if len(collisions) > 0:
                avatar.set_position(900, 250)

            deltat = clock.tick(500)
            monster_speed_scale = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill((255, 255, 255))
            pygame.draw.line(screen, (0, 0, 0), (80, 0), (80, 500), 7)
            avatar_group.update(deltat / 1000)
            monster_group.update(100, deltat / 300 * monster_speed_scale)
            avatar_group.draw(screen)
            monster_group.draw(screen)

            pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((1024, 500))
Game().main(screen)
