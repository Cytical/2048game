#2048 game by ezraguiao
#finished 4/21/20

import numpy as np 
import pygame
import random 
import os
import sys

pygame.init()

bluetheme = True
redtheme = False

WHITE = (255,255,255)
GREY = (128,128,128)
BLACK = (0,0,0)
ROW_COUNT = 4
COLUMN_COUNT = 4
SQUARE_SIZE = 180

screen_width= 727
screen_height= 900
score = 0
highscore = 0

running = True
game_still_going = True


board = np.zeros((ROW_COUNT,COLUMN_COUNT) , dtype = int)  

def display_message(msg,x,y,z,color):
    font = pygame.font.Font("freesansbold.ttf",z)
    text = font.render(msg, False, color, )
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
#spawning 
def spawn_number(x, y):
    global score
    random_spawn_one = random.randrange(0,4)
    random_spawn_two = random.randrange(0,4)
    check_gamestate()
    if game_still_going:
        if board[random_spawn_one, random_spawn_two] == 0:
            board[random_spawn_one, random_spawn_two] = x + y
        else:
            spawn_in_board()
        score = score + x + y
    else:
        return


def spawn_in_board():
    if random.randrange(0,4) >= 1:
        spawn_number(2,0)
    else:
        spawn_number(0,4)

def check_gamestate():
    global game_still_going 
    #wrong coding as of now
    if board[0][0] != 0 and board[1][0] != 0 and board[2][0] != 0 and board[3][0] != 0 and board[0][1] != 0 and board[1][1] != 0 and board[2][1] != 0 and board[3][1] != 0 and board[0][2] != 0 and board[1][2] != 0 and board[2][2] != 0 and board[3][2] != 0 and board[0][3] != 0 and board[1][3] != 0 and board[2][3] != 0 and board[3][3] != 0:
        for r in range(ROW_COUNT):  
            for c in range(COLUMN_COUNT-1): 
                if board[r][c] != board[r][c+1]:
                    for r in range(ROW_COUNT):  
                        for c in range(1,COLUMN_COUNT):  
                            if board[r][c] != board[r][c-1]:
                                for r in range(1,ROW_COUNT):  
                                    for c in range(COLUMN_COUNT):  
                                        if board[r][c] != board[r-1][c]:
                                            for r in range(ROW_COUNT-1):  
                                                 for c in range(COLUMN_COUNT):  
                                                    if board[r][c] != board[r+1][c]:
                                                        game_still_going = False
    else:
        game_still_going = True

#keyboard functions 

def  move_board_right():

    for r in range(ROW_COUNT):
                
        tile = board[r][0]
        tile2 = board[r][1]
        tile3 = board[r][2] 
        if board[r][3] == 0:
            board[r][2] = board[r][3]
            board[r][3] = tile3
                    
        if board[r][2] == 0:
            board[r][1] = board[r][2]
            board[r][2] = tile2
            if board[r][3] == 0:
                board[r][2] = board[r][3]
                board[r][3] = tile2
        
        if board[r][1] == 0:
            board[r][0] = board[r][1]
            board[r][1] = tile
            if board[r][2] == 0:
                board[r][1] = board[r][2]
                board[r][2] = tile
                if board[r][3] == 0:
                    board[r][2] = board[r][3]
                    board[r][3] = tile
        merge_tiles_right()

def  move_board_left():

    for r in range(ROW_COUNT):
                
        #tile = board[r][0]
        tile2 = board[r][1]
        tile3 = board[r][2] 
        tile4 = board[r][3]
        if board[r][0] == 0:
            board[r][1] = board[r][0]
            board[r][0] = tile2
                    
        if board[r][1] == 0:
            board[r][2] = board[r][1]
            board[r][1] = tile3
            if board[r][0] == 0:
                board[r][1] = board[r][0]
                board[r][0] = tile3
        
        if board[r][2] == 0:
            board[r][3] = board[r][2]
            board[r][2] = tile4
            if board[r][1] == 0:
                board[r][2] = board[r][1]
                board[r][1] = tile4
                if board[r][0] == 0:
                    board[r][1] = board[r][0]
                    board[r][0] = tile4
            
        merge_tiles_left()
                    
def  move_board_up():

    for c in range(COLUMN_COUNT):
                
        #tile = board[0][c]
        tile2 = board[1][c]
        tile3 = board[2][c] 
        tile4 = board[3][c]
        if board[0][c] == 0:
            board[1][c] = board[0][c]
            board[0][c] = tile2
                    
        if board[1][c] == 0:
            board[2][c] = board[1][c]
            board[1][c] = tile3
            if board[0][c] == 0:
                board[1][c] = board[0][c]
                board[0][c] = tile3
        
        if board[2][c] == 0:
            board[3][c] = board[2][c]
            board[2][c] = tile4
            if board[1][c] == 0:
                board[2][c] = board[1][c]
                board[1][c] = tile4
                if board[0][c] == 0:
                    board[1][c] = board[0][c]
                    board[0][c] = tile4
        merge_tiles_up()

def  move_board_down():

    for c in range(COLUMN_COUNT):
                
        tile = board[0][c]
        tile2 = board[1][c]
        tile3 = board[2][c] 
        #tile4 = board[3][c]
        if board[3][c] == 0:
            board[2][c] = board[3][c]
            board[3][c] = tile3
                    
        if board[2][c] == 0:
            board[1][c] = board[2][c]
            board[2][c] = tile2
            if board[3][c] == 0:
                board[2][c] = board[0][c]
                board[3][c] = tile2
        
        if board[1][c] == 0:
            board[0][c] = board[1][c]
            board[1][c] = tile
            if board[2][c] == 0:
                board[1][c] = board[2][c]
                board[2][c] = tile
                if board[3][c] == 0:
                    board[2][c] = board[0][c]
                    board[3][c] = tile
        merge_tiles_down()

def merge_tiles_right():
    for r in range(ROW_COUNT):  
        for c in range(COLUMN_COUNT-1):  
            if board[r][c] == board[r][c+1] and board[r][c+1] != 0:
                board[r][c+1] *= 2
                board[r][c] = 0

def merge_tiles_left():
    for r in range(ROW_COUNT):  
        for c in range(1,COLUMN_COUNT):  
            if board[r][c] == board[r][c-1] and board[r][c-1] != 0:
                board[r][c-1] *= 2
                board[r][c] = 0
                
def merge_tiles_up():
    for r in range(1,ROW_COUNT):  
        for c in range(COLUMN_COUNT):  
            if board[r][c] == board[r-1][c] and board[r-1][c] != 0:
                board[r-1][c] *= 2
                board[r][c] = 0

def merge_tiles_down():
    for r in range(ROW_COUNT-1):  
        for c in range(COLUMN_COUNT):  
            if board[r][c] == board[r+1][c] and board[r+1][c] != 0:
                board[r+1][c] *= 2
                board[r][c] = 0
        


def keyboard_move():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_board_up()
                spawn_in_board()
            elif event.key == pygame.K_DOWN:
                move_board_down()
                spawn_in_board()
            elif event.key == pygame.K_LEFT:
                move_board_left()
                spawn_in_board()
            elif event.key == pygame.K_RIGHT:
                move_board_right()
                spawn_in_board()
            elif event.key == pygame.K_SPACE:
                global board
                global score
                screen_theme_blue
                board = np.zeros((ROW_COUNT,COLUMN_COUNT) , dtype = int) 
                score = 0
                spawn_in_board()
                spawn_in_board()
            else: 
                keyboard_move()
                
def high_score():
    global highscore
    global score
    display_message("High Score: ",100,20,30,BLACK)

    if score > highscore:
        highscore = score

    elif score < highscore:
        highscore = highscore
    display_message(str(highscore),210,20,30,BLACK)


screen=pygame.display.set_mode((screen_width,screen_height))

pygame.mouse.set_visible(True)
pygame.display.set_caption("2048 game by ezraguiao")


def screen_theme_blue():

    global redtheme
    global bluetheme
    redtheme = False
    bluetheme = True
    screen.fill((122,215,237))
    display_message("Theme - Press T",580,20,30,(255,0,0))
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 0:
                pygame.draw.rect(screen, (201,239,248), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
            if board[r][c] == 2:
                pygame.draw.rect(screen, (224,255,255), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("2",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)
            if board[r][c] == 4:
                pygame.draw.rect(screen, (209,255,255), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("4",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 8:
                pygame.draw.rect(screen, (194,248,246), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("8",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 16:
                pygame.draw.rect(screen, (180,233,231), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("16",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 32:
                pygame.draw.rect(screen, (166,218,216), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("32",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 64:
                pygame.draw.rect(screen, (138,189,188), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("64",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 128:
                pygame.draw.rect(screen, (48,191,191), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("128",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 256:
                pygame.draw.rect(screen, (36,91,91), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("256",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 512:
                pygame.draw.rect(screen, (69,88,89), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("512",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 1024:
                pygame.draw.rect(screen, (24,47,47), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("1024",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 2048:
                pygame.draw.rect(screen, (107,142,35), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("2048",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)   

def screen_theme_red():
    global redtheme
    global bluetheme
    redtheme = True
    bluetheme = False
    screen.fill((203,137,125))
    display_message("Theme - Press T",580,20,30,(0,0,255))
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 0:
                pygame.draw.rect(screen, (226,190,183), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
            if board[r][c] == 2:
                pygame.draw.rect(screen, (255,225,220), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("2",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)
            if board[r][c] == 4:
                pygame.draw.rect(screen, (252,196,186), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("4",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 8:
                pygame.draw.rect(screen, (247,166,154), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("8",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 16:
                pygame.draw.rect(screen, (239,136,122), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("16",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 32:
                pygame.draw.rect(screen, (229,105,91), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("32",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 64:
                pygame.draw.rect(screen, (217,70,62), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("64",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 128:
                pygame.draw.rect(screen, (178,60,52), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("128",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 256:
                pygame.draw.rect(screen, (140,50,43), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("256",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 512:
                pygame.draw.rect(screen, (105,40,34), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("512",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)  
            if board[r][c] == 1024:
                pygame.draw.rect(screen, (71,30,25), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("1024",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK) 
            if board[r][c] == 2048:
                pygame.draw.rect(screen, (39,19,16), (7+SQUARE_SIZE*c,SQUARE_SIZE+SQUARE_SIZE*r,SQUARE_SIZE-7,SQUARE_SIZE-7))
                display_message("2048",int((c+1)*SQUARE_SIZE-80),int((r+1)*SQUARE_SIZE+80),52,BLACK)   

def change_theme():
    global redtheme
    global bluetheme
    if redtheme:
        screen_theme_blue()
    elif bluetheme:
        screen_theme_red()

def misc():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                change_theme()

#starting pieces
for x in range(2):
    spawn_in_board() 

while running:

    if redtheme:
        screen_theme_red()
    elif bluetheme:
        screen_theme_blue()
    
    high_score()

    if not game_still_going :
        screen.fill(WHITE)
        display_message("game over",ROW_COUNT*SQUARE_SIZE//2, screen_height//2 - 100, 70,BLACK)
        display_message("Spacebar - Play Again",ROW_COUNT*SQUARE_SIZE//2, screen_height//2 + 100, 50,BLACK)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.time.delay(10)
                    screen_theme_blue
                    board = np.zeros((ROW_COUNT,COLUMN_COUNT) , dtype = int) 
                    score = 0
                    game_still_going = True
                    spawn_in_board()
                    spawn_in_board()

    if game_still_going:
        keyboard_move()
    display_message(str(score), (ROW_COUNT*SQUARE_SIZE)//2, 100, 40,BLACK)

    misc()
    
    pygame.display.update()


#To play terminal version remove 'not' from below V
while not True:
    player_move = int(input("1- left 2-right 3-up 4-down "))
    if player_move == 1:
        os.system('cls')
        move_board_left()
        spawn_in_board()
        print(board)
        print()
        
    if player_move == 2:
        os.system('cls')
        move_board_right()
        spawn_in_board()
        print(board)
        print()
    if player_move == 3:
        os.system('cls')
        move_board_up()
        spawn_in_board()
        print(board)
        print()
    if player_move == 4:
        os.system('cls')
        move_board_down()
        spawn_in_board()
        print(board)
        print()
    else:
        continue