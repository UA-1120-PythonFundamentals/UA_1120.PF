import pygame
import sys
import random
import pygame_menu

pygame.init()

# Set up screen size and caption
SIZE_BLOCK = 20
COUNT_BLOCK = 20
HEADER_MARGIN = 70
MARGIN = 1
size = [SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK,
        SIZE_BLOCK * COUNT_BLOCK + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCK + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake game")

# Set up colors
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)

# Set up fonts
courier = pygame.font.SysFont("courier", 36)

# Snake block class
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCK and 0 <= self.y < COUNT_BLOCK

    def update_position(self):
        self.x = (self.x + COUNT_BLOCK) % COUNT_BLOCK
        self.y = (self.y + COUNT_BLOCK) % COUNT_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

# Draw a single block on the screen
def draw_block(color, row, column):
    pygame.draw.rect(screen, color, (SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK))

# Display crash message
def display_crash_message(total):
    game_over_text = courier.render("Game Over", True, RED)
    game_over_rect = game_over_text.get_rect(center=(size[0] // 2, size[1] // 2 - 20))
    screen.blit(game_over_text, game_over_rect)

    score_text = courier.render(f"Your score: {total}", True, RED)
    score_rect = score_text.get_rect(center=(size[0] // 2, size[1] // 2 + 20))
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.time.delay(5000)
    return False

def set_difficulty(selected_difficulty, value):
    if selected_difficulty == 0:  # Hard
        return 0
    elif selected_difficulty == 1:  # Easy
        return 1

# Start the game function
def start_the_game(selected_difficulty, text_input):
    player_name = text_input.get_value()
    running = True

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCK - 1)
        y = random.randint(0, COUNT_BLOCK - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_block:
            empty_block.x = random.randint(0, COUNT_BLOCK - 1)
            empty_block.y = random.randint(0, COUNT_BLOCK - 1)
        return empty_block

    snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1
    timer = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exit")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        screen.blit(screen, (0, HEADER_MARGIN))

        text_total = courier.render(f"Total: {total}", 0, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
        text_name = courier.render(f"Player: {player_name}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK + 10))
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))
        screen.blit(text_name, (SIZE_BLOCK, HEADER_MARGIN - 75))

        for row in range(COUNT_BLOCK):
            for column in range(COUNT_BLOCK):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE

                draw_block(color, row, column)

        head = snake_block[-1]
        if not head.is_inside():
            running = display_crash_message(total)
            break

        draw_block(RED, apple.x, apple.y)
        for block in snake_block:
            draw_block(SNAKE_COLOR, block.x, block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            if selected_difficulty == 0:
                speed = total // 2 + 1
            elif selected_difficulty == 1:
                if total % 3 == 0:
                    speed = total // 3 + 1
            snake_block.append(apple)
            apple = get_random_empty_block()

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock((head.x + d_row) % COUNT_BLOCK, (head.y + d_col) % COUNT_BLOCK)

        if new_head in snake_block:
            running = display_crash_message(total)

        snake_block.append(new_head)
        snake_block.pop(0)

        timer.tick(3 + speed)

# Main menu
menu = pygame_menu.Menu("Welcome", 460, 530,
                        theme=pygame_menu.themes.THEME_BLUE)

text_name = menu.add.text_input("Please enter your name: ", default="")
menu.add.selector('Difficulty :', [('Hard', 0), ('Easy', 1)], onchange=set_difficulty)
menu.add.button("Play", start_the_game, 0, text_name)
menu.add.button("Quit", pygame_menu.events.EXIT)

menu.mainloop(screen)