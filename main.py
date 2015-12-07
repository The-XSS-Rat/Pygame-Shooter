import pygame
import random
import clBullet,clBlock,clPlayer,clWalls
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255) 

#The array that holds all the walls
walls = []

# --- Create the window

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W     W     W             W                W",
"W     W     W             W                W",
"W     W     W             W                W",
"W     W     WWWWWWWWWW    WWWWWWWWWWWWWW   W",
"W     W                        W           W",
"W     WWWWWWWWWWWWWWWW         W           W",
"W                              W           W",
"W                              W           W",
"W     WWWWWWWWWWWWWWWW         W           W",
"W     W              W         W           W",
"W     W              W         W           W",
"W     W              W         W           W",
"W     W              W         W           W",
"W     WWWWWWWWWWWWWWWW         W           W",
"W                          WWWWWWWWWWWWW   W",
"W                                          W",
"W                                          W",
"W     WWWWWWWWWWWWWWWW                     W",
"W     W              W          WWWWWWWWWWWW",
"W     W              W                     W",
"W     W              W                     W",
"W     W              W                     W",
"W                    W                     W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#Create a random level
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

for i in range(12):
    strLevelAdd = "W"
    for j in range(21):
        if random.randint(0,100) > 20:
            strLevelAdd = strLevelAdd + "  "
        else:
            strLevelAdd = strLevelAdd + "WW"
        strLevelAdd = strLevelAdd[:]
        print(strLevelAdd)
    level.append(strLevelAdd + "WW")
    level.append(strLevelAdd + "WW")
del level[-1]
level.append("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")

 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = clBlock.Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
    
    block.setXY(block.rect.x,block.rect.y)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = clPlayer.Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370

#Fill the walls array
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            walls.append(clWalls.Wall((x, y)))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
    
    
player.setWalls(walls)
block.setWalls(walls)
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bullet = clBullet.Bullet("left")
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if event.key == pygame.K_RIGHT:
                bullet = clBullet.Bullet("right")
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if event.key == pygame.K_UP:
                bullet = clBullet.Bullet("up")
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            if event.key == pygame.K_DOWN:
                bullet = clBullet.Bullet("down")
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = clBullet.Bullet("up")
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
    
    # For each block, set the new target
    for block in block_list:
        block.set_target((player.rect.x,player.rect.y))
        
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
    # --- Draw a frame
     
    # Clear the screen
    screen.fill(WHITE)
    
    
    # Draw the levels walls
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall.rect)

    # Draw all the spites
    all_sprites_list.draw(screen)
    
    #Check for collisions of player with enemy
    collisions = pygame.sprite.spritecollide(player,block_list,False)     #argument one is the sprite, argument two is the group to test collisions with the sprite for, and the final argument should almost always be False, because when it is True, colliding sprites will automatically get deleted.
    for block in collisions:                                              #Spritecollide returns a list of colliding sprites. This will iterate through them.
        if block != player:                                             #spritecollide will also always return that the sprite is colliding with itself. this will filter that out, because you don't want this information.
            print("collision detected, insert code to run on collision here or return True from a function")
            block_list.remove(block)
            all_sprites_list.remove(block)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(180)
 
pygame.quit()
