import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Number Guessing Game")

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 36)
message_font = pygame.font.Font(None, 36)

target_number = random.randint(1, 100)
attempts = 0

input_box = pygame.Rect(width // 2 - 100, height // 2 - 15, 200, 30)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

message_text_line = "Please enter your number from range 1 to 100"
message_render_line = message_font.render(message_text_line, True, black)

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        user_guess = int(text)
                        attempts += 1

                        message_text_line = " "
                        message_render_line = message_font.render(message_text_line, True, black)

                        if user_guess == target_number:
                            print("Congratulations! You guessed the number.")
                            pygame.quit()
                            sys.exit()
                        elif user_guess < target_number:
                            hint_text = "The number is greater. Attempts left: {}".format(10 - attempts)
                        else:
                            hint_text = "The number is smaller. Attempts left: {}".format(10 - attempts)

                    except ValueError:
                        hint_text = "Invalid input. Please enter a valid number. Attempts left: {}".format(10 - attempts)

                    if attempts == 10:
                        print(f"Sorry! You've used all your attempts. The correct number was {target_number}. Better luck next time!")
                        pygame.quit()
                        sys.exit()                  

                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.blit(message_render_line, (width // 0.5 - message_render_line.get_width() // 2, input_box.y + 100))                 

    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    if attempts > 0:
        hint_render = font.render(hint_text, True, black)
        screen.blit(hint_render, (screen.get_width() // 2 - hint_render.get_width() // 2, height // 2 + 30))

    pygame.display.flip()