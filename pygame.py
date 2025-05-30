from re import A
import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (240, 30, 30)
green = (0, 255, 0)
blue = (50, 120, 220)
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake and Food')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("Comic Sans MS", 35)
a=0
b_font=pygame.font.SysFont("Comic Sans MS",25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
def high_score(b,color):
    highscore = b_font.render("high score: " + str(b),True,color)
    dis.blit(highscore,[dis_width / 5, dis_height / 2])
def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def message(msg, color):    
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
     
highest_score=[0]

def gameLoop():
    
    
    
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    
    food1x = round(random.randrange(0, dis_width) / 10.0)*10.0
    food1y = round(random.randrange(0, dis_height) / 10.0)*10.0 
    
    while game_over==False:
        while game_close == True:
            b=max(highest_score)
            dis.fill(blue)
            
           
            message("You Lost! Press C to Play Again or Q to Quit", red)
            
            high_score(str(b),red)
            Your_score(Length_of_snake - 1)
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [food1x, food1y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == food1x and y1 == food1y:
            food1x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food1y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        highest_score.append(Length_of_snake-1)  
        
        
        clock.tick(snake_speed)
    
           
    pygame.quit()
    quit()
    

gameLoop()