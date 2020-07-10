import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 15, 23, 45)
    
    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 15, 23, 45)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-5", 1, (255, 0, 0))
        win.blit(text, (400 - text.get_width()/2, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class Projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy:
    walkRight = [pygame.image.load('Juego/Game/R1E.png'), pygame.image.load('Juego/Game/R2E.png'), pygame.image.load('Juego/Game/R3E.png'), pygame.image.load('Juego/Game/R4E.png'), pygame.image.load('Juego/Game/R5E.png'), pygame.image.load('Juego/Game/R6E.png'), pygame.image.load('Juego/Game/R7E.png'), pygame.image.load('Juego/Game/R8E.png'), pygame.image.load('Juego/Game/R9E.png'), pygame.image.load('Juego/Game/R10E.png'), pygame.image.load('Juego/Game/R11E.png')]
    walkLeft = [pygame.image.load('Juego/Game/L1E.png'), pygame.image.load('Juego/Game/L2E.png'), pygame.image.load('Juego/Game/L3E.png'), pygame.image.load('Juego/Game/L4E.png'), pygame.image.load('Juego/Game/L5E.png'), pygame.image.load('Juego/Game/L6E.png'), pygame.image.load('Juego/Game/L7E.png'), pygame.image.load('Juego/Game/L8E.png'), pygame.image.load('Juego/Game/L9E.png'), pygame.image.load('Juego/Game/L10E.png'), pygame.image.load('Juego/Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.health = 9
        self.visible = True
        self.hitbox = (self.x + 18, self.y, 23, 55)

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 11:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount], (self.x, self.y))
                self.walkCount +=1
            else:
                win.blit(self.walkLeft[self.walkCount], (self.x, self.y))
                self.walkCount +=1
            pygame.draw.rect(win,(255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win,(0,125 ,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5*(9-self.health)), 10))
        self.hitbox = (self.x + 18, self.y, 23, 55)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render("Score: " + str(score), 1, (0,0,0))
    win.blit(text, (750, 10))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    goblin.draw(win)
    pygame.display.update()

pygame.init()
screenwidth = 850
screenheight = 480
win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Juego/Game/Right/R1.png'), pygame.image.load('Juego/Game/Right/R2.png'), pygame.image.load('Juego/Game/Right/R3.png'), pygame.image.load('Juego/Game/Right/R4.png'), pygame.image.load('Juego/Game/Right/R5.png'), pygame.image.load('Juego/Game/Right/R6.png'), pygame.image.load('Juego/Game/Right/R7.png'), pygame.image.load('Juego/Game/Right/R8.png'), pygame.image.load('Juego/Game/Right/R9.png')]
walkLeft = [pygame.image.load('Juego/Game/Left/L1.png'), pygame.image.load('Juego/Game/Left/L2.png'), pygame.image.load('Juego/Game/Left/L3.png'), pygame.image.load('Juego/Game/Left/L4.png'), pygame.image.load('Juego/Game/Left/L5.png'), pygame.image.load('Juego/Game/Left/L6.png'), pygame.image.load('Juego/Game/Left/L7.png'), pygame.image.load('Juego/Game/Left/L8.png'), pygame.image.load('Juego/Game/Left/L9.png')]
bg = pygame.image.load('Juego/Game/bg.jpg')
char = pygame.image.load('Juego/Game/standing.png')

bulletsound = pygame.mixer.Sound("Juego/Game/bullet.wav")
hitsound = pygame.mixer.Sound("Juego/Game/hit.wav")

music = pygame.mixer.music.load("Juego/Game/music.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

score = 0

# -------------- mainloop -------------- #
font = pygame.font.SysFont("comicsans", 15, True)

man = Player(300, 410, 64, 64)
goblin = Enemy(50, 416, 64, 64, 750)
bullets = []
shootloop = 0
run = True
while run:
    clock.tick(27)
    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and goblin.visible:
                hitsound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if 0 < bullet.x < 850:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop == 0:
        bulletsound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width//2), round(man.y + man.height//2),6, (255,0,0), facing))
        shootloop = 1

    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < (screenwidth - man.width):
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= man.jumpCount**2 / 2 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()