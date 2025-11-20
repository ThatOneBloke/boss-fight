import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))
bossx = 100
bossy = 400
playerx = 400
playery = 400
playerhealth = 100
hit = False
isjumping = False

boss = pygame.Rect(bossx, bossy, 50, 50)
player = pygame.Rect(playerx, playery, 30, 50)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("grey")
    pygame.draw.rect(screen, "green", boss)
    pygame.draw.rect(screen, "blue", player)
    #if not hit:
        #if bossx < playerx:
            #bossx += 20
        #elif bossx > playerx:
            #bossx -= 2
    #if boss.colliderect(player):
        #hit = True
    #if hit:
        #playerhealth -= 10
        #if playerx <= bossx:
            #player.x -= 20
        #elif playerx >= bossx:
            #player.x += 20
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 2
    elif keys[pygame.K_d]:
        player.x += 2
    elif keys[pygame.K_SPACE]:
        isjumping = True
        if isjumping == True:
            player.y -= 10
    pygame.display.update()