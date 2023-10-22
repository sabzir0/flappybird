import pygame


WIDHT = 1300
HEIGHT = 600

SIZE = (WIDHT,HEIGHT)

window = pygame.display.set_mode(SIZE)
background_color = (255,0,0)
window.fill(background_color)
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size, speed):
        self.image = pygame.Surface(size=size, masks=(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bird(GameSprite):
    def update(self):
        self.rect.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.y -= self.speed*2




bird = Bird(None, (0, HEIGHT/2), (50,50), 5)


game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.fill(background_color)
    bird.update()
    bird.reset()

    pygame.display.update()
    clock.tick(60)
