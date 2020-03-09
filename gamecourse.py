import pygame 
import random 

pygame.init() 

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) 

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("player.jpg")
enemy2 = pygame.image.load("monster.jpg")

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

playerXPosition = 100
playerYPosition = 50

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

while 1: 

    screen.fill(0) 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyUp = False
            if event.key == pygame.K_RIGHT:
                keyDown = False 
    
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
    
    playerBox = pygame.Rect(player.get_rect()) 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    if playerBox.colliderect(enemyBox):
        if playerBox.colliderect(enemy1Box):
            if playerBox.colliderect(enemy2Box):
        
                print("You lose!")
        
        pygame.quit()
        exit(0)
    
    if enemyXPosition < 0 - enemy_width:
        if enemy1XPosition < 0 - enemy1_width:
            if enemy2XPosition < 0 - enemy2_width:
        
                print("You win!")
        
        pygame.quit()
        
        exit(0)
    
    enemyXPosition -= 0.15
    enemy1XPosition -= 0.65
    enemy2XPosition -= 0.50
    

  
