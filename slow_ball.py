import pygame,random
pygame.init()
width=550
height=550
fps=60
overloads=False
gamefps=pygame.time.Clock()
green=(0,255,0)
laser_option=random.randint(50,100)
gamewindow=pygame.display.set_mode((width,height))
def text_screen(text, color, x, y,bsize):
    font = pygame.font.SysFont(None, bsize)
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])
class ball:
    ball_x,ball_y,vel,x,envel,enemy_x,enemy_y,i,ok,bar_vel,radius=250,250,6,0,6,random.randint(25,525),0,0,True,4,15
    def moving(self):   
        pygame.draw.circle(gamewindow, (0, 0, 255), (self.ball_x, self.ball_y), self.radius)
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_RIGHT] and self.ball_x<525:
            self.ball_x+=self.vel
        if userinput[pygame.K_LEFT] and self.ball_x>25:
            self.ball_x-=self.vel
        if userinput[pygame.K_UP] and self.ball_y>25:
            self.ball_y-=self.vel
        if userinput[pygame.K_DOWN] and self.ball_y<525:
            self.ball_y+=self.vel
        if userinput[pygame.K_SPACE] and self.x>=-1  and self.ok:
            self.x+=self.bar_vel*3
            pygame.draw.rect(gamewindow,(200,49,255),(0,height-10,self.x,10))
        if not userinput[pygame.K_SPACE] and self.x>0 and self.ok:
            self.x-=self.bar_vel*3
            pygame.draw.rect(gamewindow,(200,49,25),(0,height-10,self.x,10))
        if self.x>=height:
            self.ok=False
            global overloads
            overloads=True
        if not self.ok and self.x>0:
            self.x-=self.bar_vel*3
            pygame.draw.rect(gamewindow,(200,49,25),(0,height-10,self.x,10))
        if self.x<=0:
            self.ok=True
            overloads=False
class enemy_ball_top(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_y+=self.envel
        if self.enemy_y>=525:
            self.enemy_y=random.randint(-150,0)
            self.enemy_x=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE] and not overloads:
            self.envel=.5
        else:
            self.envel=random.randint(6,10)
class enemy_ball_left(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_x+=self.envel
        if self.enemy_x>=525:
            self.enemy_x=random.randint(-150,0)
            self.enemy_y=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE] and not overloads:
            self.envel=.5
        else:
            self.envel=random.randint(6,10)
class enemy_ball_right(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_x-=self.envel
        if self.enemy_x<=25:
            self.enemy_x=random.randint(525,700)
            self.enemy_y=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE] and not overloads:
            self.envel=.5
        else:
            self.envel=random.randint(6,10)
class enemy_ball_bottom(ball):
    def enemy(self):
        pygame.draw.circle(gamewindow,(255,0,0),(self.enemy_x,self.enemy_y),5)
        self.enemy_y-=self.envel
        if self.enemy_y<=25:
            self.enemy_y=random.randint(600,650)
            self.enemy_x=random.randint(25,525)
            self.i+=1
        userinput=pygame.key.get_pressed()
        if userinput[pygame.K_SPACE] and not overloads:
            self.envel=.5
        else:
            self.envel=random.randint(6,10)
player=ball()
enem=enemy_ball_top()
a,b,c,d,e,f,k,j,l,m=enemy_ball_top(),enemy_ball_left(),enemy_ball_right(),enemy_ball_bottom(),enemy_ball_right(),enemy_ball_top(),enemy_ball_right(),enemy_ball_left(),enemy_ball_left(),enemy_ball_bottom()
def gameloop():
    run,gameover,homescreen,go,laser,laser1,laser2 = True,False,False,True,False,False,False
    y1,yl1,yl2,xl1,xl2=230,0,height,width,0
    but_color,other_but_color=(0,200,0),(0,0,200)
    while run:
        gamewindow.fill((255,255,255))
        if laser:
            yl1_vel=.5
            if yl1<100 and go:
                yl1+=yl1_vel
                yl2-=yl1_vel
                xl1-=yl1_vel
                xl2+=yl1_vel
            else:
                go=False
                yl1-=yl1_vel
                yl2+=yl1_vel
                xl1+=yl1_vel
                xl2-=yl1_vel
                if yl1<=0:
                    go=True
                    laser=False
            pygame.draw.line(gamewindow,(90,68,159),(0,yl1),(550,yl1),5)
            pygame.draw.line(gamewindow,(90,68,159),(0,yl2),(550,yl2),5) 
            pygame.draw.line(gamewindow,(90,68,159),(xl1,0),(xl1,550),5)
            pygame.draw.line(gamewindow,(90,68,159),(xl2,0),(xl2,550),5)  
        if laser1:
            yl1_vel=.5
            if xl2<100 and go:
                xl1-=yl1_vel
                xl2+=yl1_vel
            else:
                go=False
                xl1+=yl1_vel
                xl2-=yl1_vel
                if xl1<=0:
                    yl1_vel=0
                    go=False
                    laser1=False
            pygame.draw.line(gamewindow,(90,68,159),(xl1,0),(xl1,550),5)
            pygame.draw.line(gamewindow,(90,68,159),(xl2,0),(xl2,550),5)
        if laser2:
            yl1_vel=.5
            if yl1<100 and go:
                yl1+=yl1_vel
                yl2-=yl1_vel
            else:
                go=False
                yl1-=yl1_vel
                yl2+=yl1_vel
                if yl1<=0:
                    yl1_vel=0
                    laser2=False
            pygame.draw.line(gamewindow,(90,68,159),(0,yl1),(550,yl1),5)
            pygame.draw.line(gamewindow,(90,68,159),(0,yl2),(550,yl2),5) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        if gameover == True and homescreen:
            gamewindow.fill((0,0,0))
            text_screen("Game over", (255,0,0), 150, 250,75)
            text_screen("your score:"+str(enem.i), (255,0,0),100, 300,75)
            text_screen("Press backspace to exit",(255,0,0),100,500,40)
            userinput=pygame.key.get_pressed()
            if userinput[pygame.K_BACKSPACE]:
                break
        elif not homescreen:
            text_screen("PLAY |>", but_color, 150, 250,75)
            text_screen("EXIT -_-", other_but_color,150, 350,75)
            pygame.draw.rect(gamewindow,(20,49,250),(130,y1,260,80),2)
            userinput=pygame.key.get_pressed()
            if userinput[pygame.K_DOWN]:
                y1=330
                but_color=(0,0,200)
                other_but_color=(0,200,0)
            elif userinput[pygame.K_UP]:
                y1=230
                but_color=(0,200,0)
                other_but_color=(0,0,200)
            elif userinput[pygame.K_SPACE] and y1==230:
                homescreen=True
            elif userinput[pygame.K_SPACE] and y1==330:
                run=False
        else:
            text_screen("Your Score: "+str(enem.i),(255,0,0),0,0,40)
            if player.x>width:
                player.bar_vel=-2
            elif player.x<=0:
                player.bar_vel=2
            player.moving()
            enem.enemy()
            if enem.i>2:
                a.enemy()
            if enem.i>5: 
                b.enemy()
            if enem.i>9:
                if laser_option%2==0:
                    laser1=True
                else:
                    laser2=True
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
            if enem.i>20:
                l.enemy()
            if enem.i>24:
                laser=True
                m.enemy()
            if abs(player.ball_x-enem.enemy_x)<player.radius+5 and abs(player.ball_y-enem.enemy_y)<player.radius+5 or (abs(player.ball_x - a.enemy_x) < player.radius+5 and abs(player.ball_y - a.enemy_y) <player.radius+5) or (abs(player.ball_x-b.enemy_x)<player.radius+5 and abs(player.ball_y-b.enemy_y)<player.radius+5) or (abs(player.ball_x-c.enemy_x)<player.radius+5 and abs(player.ball_y-c.enemy_y)<player.radius+5) or (abs(player.ball_x-d.enemy_x)<player.radius+5 and abs(player.ball_y-d.enemy_y)<player.radius+5) or (abs(player.ball_x-e.enemy_x)<player.radius+5 and abs(player.ball_y-e.enemy_y)<player.radius+5) or (abs(player.ball_x-f.enemy_x)<player.radius+5 and abs(player.ball_y-f.enemy_y)<player.radius+5) or (abs(player.ball_x-j.enemy_x)<player.radius+5 and abs(player.ball_y-j.enemy_y)<player.radius+5) or (abs(player.ball_x-k.enemy_x)<player.radius+5 and abs(player.ball_y-k.enemy_y)<player.radius+5) or abs(player.ball_y-yl1)<player.radius:
                gameover = True
            if abs(player.ball_x-l.enemy_x)<player.radius+5 and abs(player.ball_y-l.enemy_y)<player.radius+5 or abs(player.ball_x-m.enemy_x)<player.radius+5 and abs(player.ball_y-m.enemy_y)<player.radius+5 or abs(player.ball_y-yl1)<player.radius or abs(player.ball_y-yl2)<player.radius or  abs(player.ball_x-xl1)<player.radius or abs(player.ball_x-xl2)<player.radius:
                gameover=True
        gamefps.tick(fps)
        pygame.display.update()
gameloop()
pygame.quit()
