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
"W     WW                                   W",
"W     WW                                   W",
"W     WW                                   W",
"W     WW                                   W",
"W     WW                                   W",
"W     WWWWWWWWWWWWWWWW                     W",
"W                                          W",
"W                                          W",
"W     WWWWWWWWWWWWWWWW                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W     WWWWWWWWWWWWWWWW                     W",
"W                                          W",
"W                                          W",
"W                                          W",
"W     WWWWWWWWWWWWWWWW                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W     WW             W                     W",
"W                    W                     W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
 
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
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = clBullet.Bullet()
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
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
