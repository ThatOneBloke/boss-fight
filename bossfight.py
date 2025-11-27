import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Boss fight")
namefont = pygame.font.SysFont("Ariel", 25)
hpnumberfont = pygame.font.SysFont("Ariel", 40)
bossname = namefont.render("boss hp: ", True, "grey")
bossx = 400
bossy = 300
playerx = 650
playery = 450
swordx = playerx - 24
swordy = playery + 23
playerhealth = 100
bosshealth = 5000
bosshpbarwidth = 810
hit = False
isjumping = False
hpnumber = hpnumberfont.render(str(bosshealth) + " / 5000", True, "black")
ground = pygame.Rect(0, 500, 1000, 200)
sword = pygame.Rect(swordx, swordy, 40, 10)
boss = pygame.Rect(bossx, bossy, 200, 200)
bgbosshpbar = pygame.Rect(95, 519, bosshpbarwidth, 60)
bosshpbar = pygame.Rect(100, 525, 800, 50)
player = pygame.Rect(playerx, playery, 30, 50)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 1
        playerx -= 1
        sword.x -= 1
    elif keys[pygame.K_d]:
        player.x += 1
        playerx += 1
        sword.x += 1
    if keys[pygame.K_SPACE] and sword.colliderect(boss):
        bosshealth -= 1
    #elif keys[pygame.K_SPACE] and keys[pygame.K_LSHIFT]:
        #if sword.colliderect(boss):
            #bosshealth -= 50
    screen.fill("grey")
    pygame.draw.rect(screen, "black", ground)
    pygame.draw.rect(screen, "grey", bgbosshpbar)
    screen.blit(bossname, (470, 500))
    pygame.draw.rect(screen, "red", bosshpbar)
    screen.blit(hpnumber, (430, 540))
    pygame.draw.rect(screen, "red", boss)
    pygame.draw.rect(screen, "green", player)
    pygame.draw.rect(screen, "blue", sword)
    pygame.display.update()