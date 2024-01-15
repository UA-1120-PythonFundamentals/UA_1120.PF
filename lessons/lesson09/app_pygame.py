import pygame

pygame.init()


gameDisplay = pygame.display.set_mode((800,600)) 

pygame.display.set_caption('My first game')



WHITE = (255, 255, 255)
Aqua  = ( 0, 255, 255)
font = pygame.font.SysFont('Calibri', 25, True, False)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
read = 0
green = 0
blue = 0
points = []


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        # print(event)
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event)
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print(event)
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            print(event)
            if event.dict.get("button") == 1:
                point = event.dict.get("pos")
                points.append(point)
            elif event.dict.get("button") == 3:
                point = points.pop()
                print(f"remove point {point}")
    
    # --- Game logic should go here
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # if read >= 255:
    #     read = 0
    # else:
    #     read += 1
    # gameDisplay.fill((read, green, blue))
    gameDisplay.fill(WHITE)
    
    # print(points)
    if len(points) > 2: 

        pygame.draw.polygon(gameDisplay, Aqua, points)

        for piunt in points:
            text = font.render(f"{point}",True, (0,0,0))
            gameDisplay.blit(text, point)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)