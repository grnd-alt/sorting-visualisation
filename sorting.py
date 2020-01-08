import pygame
import random
def sort(values):
    pygame.init()
    display_width = 1500
    display_height = 600
    screen = pygame.display.set_mode((display_width,display_height))
    class balken:
        def __init__(self,height,x,w):
            self.y = display_height-height
            self.height = height
            self.x = x
            self.w = w
            self.color = (0,0,0)
        def draw(self):
            pygame.draw.line(screen,self.color,(self.x,self.y),(self.x,display_height),self.w)

    x =0
    width = (display_width/len(values))
    width = int(width)
    gap = width + 1
    x += width
    balken_list = []
    for i in values:
        balken_list.append(balken(i,x,width))
        x += gap
    game = True
    frame = 0
    while game:
        frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((255,255,255))
        for i in balken_list:
            i.draw()
        if frame == 10:
            frame = 0
            doing = False
            for x,i in enumerate(balken_list):
                try:
                    if i.y < balken_list[x+1].y:
                        failsafe = balken_list[x+1].x
                        balken_list[x+1].x = i.x
                        i.x = failsafe
                        failsafe = balken_list[x+1]
                        balken_list.pop(x+1)
                        balken_list.insert(x,failsafe)
                        doing = True
                except:
                    pass
            if doing == False:
                end = []
                ave = 0
                for i in balken_list:
                    end.append(i.height)
                    for i in randoms:
                        ave += i
                    ave = ave / len(randoms)
                return str(end)+'\n'+'Average number = '+str(ave)

        pygame.display.update()
        pygame.time.Clock().tick(60)
randoms = []
for i in range(50):
    randoms.append(random.randint(0,600))
sort(randoms)