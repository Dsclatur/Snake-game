import pygame
import random
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('backkkk.mp3')
pygame.mixer.music.play()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

score=0

snake_x=45
snake_y=45
snake_size=20
velocity_x=0
velocity_y=0

snk_list=[]
snk_length=1

screen_width=1200
screen_height=700
fps=30

init_velocity=10

food_x=random.randint(0,screen_width)
food_y=random.randint(0,screen_height)

gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake with Sadik")
pygame.display.update()


clock=pygame.time.Clock()


exit_game=False
game_over=False


font=pygame.font.SysFont(None,55)
#function for score

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
    
    


while not exit_game:
    if game_over:
        gamewindow.fill(white)
        text_screen("Game Over",red,screen_width/2,screen_height/2)
        text_screen("You have Scored:"+str(score),red,screen_width/2,screen_height/2+40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            
                    
    else:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    velocity_x=init_velocity
                    velocity_y=0
                if event.key==pygame.K_LEFT:
                    velocity_x=-init_velocity
                    velocity_y=0
                if event.key==pygame.K_UP:
                    velocity_y=-init_velocity
                    velocity_x=0
                if event.key==pygame.K_DOWN:
                    velocity_y=init_velocity
                    velocity_x=0

        snake_x=snake_x+velocity_x
        snake_y=snake_y+velocity_y

        if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
            score=score+1;
           
            food_x=random.randint(0,screen_width)
            food_y=random.randint(0,screen_height)
            snk_length+=5
      
            
        gamewindow.fill(white)
        text_screen("score: "+str(score),red,370,5)
        pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])

        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
            game_over=True
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            
        
        if len(snk_list)>snk_length:
            del snk_list[0]
        plot_snake(gamewindow,black,snk_list,snake_size)
    pygame.display.update()
    clock.tick(fps)



    
pygame.quit()
quit()

         


    
