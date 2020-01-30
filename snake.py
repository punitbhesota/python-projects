import pygame
import random
pygame.init()
pygame.mixer.music.load("C:\\gui\\Hindustani_bhau.mp3")
pygame.mixer.music.play()

#Creating window
screen_width = 500
screen_height = 500
window = pygame.display.set_mode((screen_width,screen_height))

#Window Title
pygame.display.set_caption("Ultimate Snake World")
pygame.display.update()

#Colors
White = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
blue  = (0,0,255)
green = (0,255,0)

#Backgrounds
bgimg = pygame.image.load("C:\\gui\\BG7.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()
bgimg2 = pygame.image.load("C:\\gui\\Gameover.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()
bgimg3 = pygame.image.load("C:\\gui\\BG3.jpg")
bgimg3 = pygame.transform.scale(bgimg3,(screen_width,screen_height)).convert_alpha()

#Game Specific Variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 35)
fps = 60

#Text function
def text_screen(text,color,x,y):                                      
    screen_text =  font.render( text , True , color ) 
    window.blit( screen_text , [x,y] )

def plot_snake( window,color, snake_list , snake_size ):
    for x,y in snake_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

#Welcome page
def startpage():
    running = True
    while running:
        window.fill((black))
        window.blit(bgimg3,(0,0))
        
        text_screen("ULTIMATE SNAKE WORLD",White,74,200)
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()
        pygame.display.update()
        clock.tick(60)    
                    
#Main function of game
def gameloop():
    with open("C:\\Users\\HP\\Downloads\\high_score.txt","r") as f:
        high_score =  f.read()
    #Variables
    running = True
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 25
    food_size = 25
    velocity_x = 0
    velocity_y = 0
    fps = 60
    score = 0  
    snake_list = []
    snake_length = 1 
    
    #Food Generation
    mango_x = random.randint(10,screen_width*0.9)
    mango_y = random.randint(10,screen_height*0.9)

    while running:
        if game_over:
            with open("C:\\Users\\HP\\Downloads\\high_score.txt","w") as f:
                f.write(str(high_score))

            window.blit(bgimg2,(0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            
            
        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT :
                        velocity_x += 5
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x -= 5
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y += 5
                        velocity_x = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y -= 5  
                        velocity_x = 0   
                    if event.key == pygame.K_a:
                        score+=50       
            snake_x += velocity_x
            snake_y += velocity_y

            #Eating Food
            if abs(snake_x - mango_x) < 15 and abs(snake_y - mango_y) < 15:
                pygame.mixer.music.load("C:\\gui\\Bagha.mp3")
                pygame.mixer.music.play()
                score += 10
                snake_length += 5
                if score > int(high_score):
                    high_score = score
                               
                mango_x = random.randint(20,screen_width*0.95)
                mango_y = random.randint(20,screen_height*0.95)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if (snake_x < 0 or snake_x > screen_width) or (snake_y < 0 or snake_y > screen_height):
                    pygame.mixer.music.load("C:\\gui\\Minions.mp3")
                    pygame.mixer.music.play()
                    game_over = True  
            if head in snake_list[:-1]:
                pygame.mixer.music.load("C:\\gui\\Minions.mp3")
                pygame.mixer.music.play()
                game_over = True
                print("game over")  
            window.fill((black))
            window.blit(bgimg,(0,0))
            text_screen("SCORE : " + str(score) + "        HIGH SCORE :" + str(high_score) , White , 5 , 5)           #onscreen text
            plot_snake(window,red, snake_list, snake_size  )                                    #snake length increasing function
            pygame.draw.rect(window,green, [ mango_x , mango_y , food_size , food_size ] )    #draws food
        pygame.display.update()
        clock.tick(fps)
         
    pygame.quit()
    quit()
startpage()