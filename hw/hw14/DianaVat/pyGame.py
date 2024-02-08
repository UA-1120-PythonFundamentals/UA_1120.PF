import pygame
import random

pygame.init()  #initialize all imported pygame modules

enterComp = random.randint(1,100)
print(enterComp) 
str_enterComp = str(f'Число, яке було загадане: {enterComp}')
#number which think computer 

screen = pygame.display.set_mode((600,400), pygame.RESIZABLE)
pygame.display.set_caption("Black Cat")
text_main = pygame.font.SysFont('arial', 24)
text_main_for_user = pygame.font.SysFont('verdana' , 20)

BLACK = (6, 7, 9)
GREY = (229, 231, 227)
RED = (175,0,0)
WHITE = (255,255,255)
GREEN = (25, 92, 44)
#colors for game

computer = text_main.render(str_enterComp, 1 , BLACK , WHITE)
position_computer = computer.get_rect(center=(600//2 ,250))

more= text_main.render("Більше", 1 , BLACK , RED)
position_more = more.get_rect(center=(600//2 ,300))
less= text_main.render("Менше", 1 , BLACK,RED)
position_less = less.get_rect(center=(600//2 ,300))

congration_no_1= text_main.render("Ти програв...", 1 , BLACK, WHITE)
position_no_congretion = congration_no_1.get_rect(center=(600//2 ,300))

congration = text_main.render("Вітання, Ви виграли!", 1 , BLACK, WHITE)
position_congration = congration.get_rect(center=(600//2 ,300))

text_condition = ["Привіт!", "Вгадай число від 1 до 100, яке загадав компьютер.", "Ти маєш 10 спроб. Удачі!"]
text_res = []

pos = 100
for text in text_condition:
    text_1 = text_main.render(text, 1 , BLACK)
    sc_text_1 = text_1.get_rect(center=(600//2 ,pos//2))
    text_res.append([text_1, sc_text_1])
    pos+=50
#"For" for positions first text

# image_icons = pygame.image.load("blc.bmp")
# pygame.display.set_icon(image_icons)
clock = pygame.time.Clock()
FPS = 60
screen.fill(GREY)
for part in text_res:
    screen.blit( part[0] , part[1])
pygame.display.update()
try_input = 0

user_enter = ''

def user_for(n=180, l=375):
        user_enter_screen = text_main_for_user.render(user_enter, 1 , BLACK , WHITE)
        position_user = user_enter_screen.get_rect(center=(n,l))
        screen.blit(user_enter_screen , position_user)
        n += 20
n=180
l=375

text_enter_user =  text_main.render("Твої відповіді: ", 1 , BLACK, WHITE)
position_answer = text_enter_user.get_rect(center=(80 ,375))
screen.blit(text_enter_user, position_answer)

while True:
    for events  in pygame.event.get():
        pygame.display.update()

        if events.type == pygame.QUIT:
            exit()
        elif events.type == pygame.KEYDOWN:

            if events.key == 13:
                if int(user_enter) == enterComp:
                    screen.blit(congration , position_congration)
                    screen.blit(computer , position_computer)
                    user_for(n, l)
                    n +=45
                    pygame.display.update()
                    pygame.time.delay(5000)
                    exit()
                   
                elif int(user_enter) < enterComp:
                    screen.blit(more , position_more)
                    user_for(n, l)
                    n +=45
                    
                else:
                    screen.blit(less , position_less)
                    user_for(n, l)
                    n +=45
                
                try_input += 1
                user_enter = ""

                if try_input >= 10:
                    screen.blit(congration_no_1 , position_no_congretion)
                    screen.blit(computer , position_computer)
                    
            elif events.unicode in ['0','1','2','3','4','5','6','7','8','9']:
                if len(user_enter) < 2:
                    user_enter += events.unicode        
    
    clock.tick(50)