import math, random, sys, keyboard, os
import pygame
from pygame.locals import *
input_file = "D:\Buller_Research\Seth_Game\Pokestats.txt"

#PokeList = [ID, Name, HP, Atk, Def, SpA, SpD, Spd, Total, Type 1, Type 2]
PokeList = []
PokeAdd = []
k = 0
with open(input_file, 'r') as load: #insert file path here
    line = load.readline()
    temp = load.readline().split()
    while len(line) > 0:
        for x in range(0,10):
            PokeAdd.append(temp[x]) # Extract Pokemon info
        if len(temp) > 10:
            PokeAdd.append(temp[10])  # In case of second type
        PokeList.append(list(PokeAdd))
        PokeAdd = []
        # load.readline()  # Skips a line
        line = load.readline()
        temp = line.split()
#hiiii

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#What is this??

print("Hallo")
# define display surface
W, H = 480, 480
SCREEN_SIZE=(480,480)
HW, HH = int(W / 2), int(H / 2)
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("SethGame #113")
FPS = 20

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)

class spritesheet:
    def __init__(self, filename, cols, rows, ID):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        self.ID = ID

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (w / 2, h / 2)
        self.cells = list([(index % cols * w, index // cols * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h), ])

    def draw(self, surface, cellIndex, x, y, handle=0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self, posx, posy, ID, Atk):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        self.ID = ID
        self.Atk = Atk

class Enemy(object):
    # sprite for the player
    def __init__(self, posx, posy, ID, Atk):
        pygame.sprite.Sprite.__init__(self)
        self.posx = posx
        self.posy = posy
        self.ID = ID
        self.Atk = Atk

class Ground:
    #ground tiles
    def __init__(self, posx, posy, type):
        self.posx = posx
        self.posy = posy
        self.type = type

        self.image = pygame.image.load('Ground1.png').convert()
        self.rect = self.image.get_rect()
s = spritesheet("Poke2.png", 12, 26, 8)

CENTER_HANDLE = 4

index = 0
player = Player(0, 0, 136,0)
enemy = Enemy(160, 160, 136,0)
ground = Ground(8,8,"normal")
j = 0
# Game loop
# Optimize the images after they're drawn
ground.image.convert()
Enemies = []
Enemies.append(Enemy(160, 160, 136,0))

while True:
    events()
    if keyboard.is_pressed('M'):
        Enemies.append(Enemy(random.randint(0,30)*16, random.randint(0,30)*16, random.randint(0,152),0))

    pygame.display.update()
    CLOCK.tick(FPS)

    # Update

    if keyboard.is_pressed('W'):
        player.posy -=16
    if keyboard.is_pressed('S'):
        player.posy += 16
    if keyboard.is_pressed('space'):
        player.ID = random.randint(0,152)
        player.Atk = PokeList[player.ID][3]
        print(player.Atk)
    if keyboard.is_pressed('A'):
        player.posx -= 16
    if keyboard.is_pressed('D'):
        player.posx += 16
    # Draw / render
    screen.fill(BLACK)

    for x in range(0, 30):
        for y in range(0, 30):
            screen.blit(ground.image, (x * 16, y * 16))

    s.draw(screen, (player.ID + index) % s.totalCellCount, player.posx, player.posy, 0)
    for i in range(0,len(Enemies)):
        if j > 2:
            Enemies[i].posx += (random.randint(-1,1)*16)
            Enemies[i].posy += (random.randint(-1, 1) * 16)
            if Enemies[i].posx < 0:
                Enemies[i].posx = 0
            elif Enemies[i].posx > W-16:
                Enemies[i].posx = W-16
            if Enemies[i].posy < 0:
                Enemies[i].posy = 0
            elif Enemies[i].posy > H-16:
                Enemies[i].posy = H-16
        s.draw(screen, (Enemies[i].ID + index) % s.totalCellCount, Enemies[i].posx, Enemies[i].posy, 0)
    j += 1
    if j > 3:
        j = 0
        index += 156
    pygame.draw.circle(screen, WHITE, (HW, HH), 2, 0)
