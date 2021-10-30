import pygame,random
pygame.init()
width=550
height=550
gamewindow=pygame.display.set_mode((width,height))
font = pygame.font.SysFont(None, 75)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])
class ball:
    ball_x=250
    ball_y=250
    vel=.3
    envel=.4
    enemy_x=random.randint(25,525)
    enemy_y=0
    i=0
    def moving(self):
        pygame.draw.circle(gamewindow, (0, 0, 255), (self.ball_x, self.ball_y), 15)
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_RIGHT] and self.ball_x<525:
            self.ball_x+=self.vel
        if userinput[pygame.K_LEFT] and self.ball_x>25:
            self.ball_x-=self.vel
        if userinput[pygame.K_UP] and self.ball_y>25:
            self.ball_y-=self.vel
        if userinput[pygame.K_DOWN] and self.ball_y<525:
            self.ball_y+=self.vel
class enemy_ball_top(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_y+=self.envel
        if self.enemy_y>=525:
            self.enemy_y=random.randint(-150,0)
            self.enemy_x=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE]:
            self.envel=.05
        else:
            self.envel=random.randint(3,10)/20
class enemy_ball_left(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_x+=self.envel
        if self.enemy_x>=525:
            self.enemy_x=random.randint(-150,0)
            self.enemy_y=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE]:
            self.envel=.05
        else:
            self.envel=random.randint(3,10)/20
class enemy_ball_right(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_x-=self.envel
        if self.enemy_x<=25:
            self.enemy_x=random.randint(525,700)
            self.enemy_y=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE]:
            self.envel=.05
        else:
            self.envel=random.randint(3,10)/20
player=ball()
enem=enemy_ball_top()
a,b,c,d,e,f,k,j=enemy_ball_top(),enemy_ball_left(),enemy_ball_right(),enemy_ball_left(),enemy_ball_right(),enemy_ball_top(),enemy_ball_right(),enemy_ball_left()
def gameloop():
    run = True
    gameover=False
    while run:
        gamewindow.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        if gameover == True:
            gamewindow.fill((0,0,0))
            text_screen("Game over", (255,0,0), 150, 250)
            text_screen("your score:"+str(enem.i), (255,0,0),100, 300)
            userinput=pygame.key.get_pressed()
            if userinput[pygame.K_SPACE]:
                run=False
        else:
            player.moving()
            enem.enemy()
            if enem.i>2:
                a.enemy()
            if enem.i>5:
                b.enemy()
            if enem.i>9:
                c.enemy()
            if enem.i>11:
                d.enemy()
            if enem.i>14:
                e.enemy()
            if enem.i>17:
                f.enemy()
            if enem.i>18:
                j.enemy()
            if enem.i>18:
                k.enemy()
            if abs(player.ball_x-enem.enemy_x)<20 and abs(player.ball_y-enem.enemy_y)<20 or (abs(player.ball_x - a.enemy_x) < 20 and abs(player.ball_y - a.enemy_y) < 20) or (abs(player.ball_x-b.enemy_x)<20 and abs(player.ball_y-b.enemy_y)<20) or (abs(player.ball_x-c.enemy_x)<20 and abs(player.ball_y-c.enemy_y)<20) or (abs(player.ball_x-d.enemy_x)<20 and abs(player.ball_y-d.enemy_y)<20) or (abs(player.ball_x-e.enemy_x)<20 and abs(player.ball_y-e.enemy_y)<20) or (abs(player.ball_x-f.enemy_x)<20 and abs(player.ball_y-f.enemy_y)<20) or (abs(player.ball_x-j.enemy_x)<20 and abs(player.ball_y-j.enemy_y)<20) or (abs(player.ball_x-k.enemy_x)<20 and abs(player.ball_y-k.enemy_y)<20):
                gameover = True
        pygame.display.update()
gameloop()