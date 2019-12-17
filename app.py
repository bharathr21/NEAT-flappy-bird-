import neat
import os
import pygame, sys
from pygame.locals import *
import random



class Bird:
	
	def __init__(self,y):
	
		self.y=y
		self.x=x
		self.jump_vel=jump_vel

	def draw(self,screen):
		bird=pygame.image.load(r'C:\Users\uic12963\Desktop\bharath\flappy bird\bird.png')
		#picture = pygame.transform.scale(bird, (20,20))
		screen.blit(bird,[self.x,self.y])


	def jump(self):
		self.y -=self.jump_vel

	def dec_jump(self):
		self.y +=self.jump_vel





def move_pipes():
	pipe_pos[0] -= 5

	upipe_pos[0] -= 5
    
def draw_pipes(screen):
    
    #if pipe_passed:
    #print("asdfjahsdlfkjahsdflkajhsdf")
    #score+=1
    
    
    
    trap=[]
    pipe=pygame.image.load(r'C:\Users\uic12963\Desktop\bharath\flappy bird\pipe.png')
    upipe=pygame.transform.flip(pipe,False,True)



    h=upipe.get_height()
    w=upipe.get_width()



    upipe2_pos=[upipe_pos[0]+GAP_BW_PIPES,upipe_pos[1]]
    pipe2_pos=[pipe_pos[0]+GAP_BW_PIPES,pipe_pos[1]]

    pipe_top=upipe_pos[1]+h
    pipe_bottom=upipe_pos[1]+h+GAP

    pipe_left=pipe_pos[0]
    pipe_right=pipe_pos[0]+w
    pipe_pos[1] =pipe_bottom




    screen.blit(upipe,upipe_pos)
    screen.blit(pipe,pipe_pos)
    #screen.blit(pipe,pipe2_pos)
    #screen.blit(upipe,upipe2_pos)

    trap=[[pipe_left,pipe_top+(GAP//2)],[pipe_right,pipe_top+(GAP//2)]]


    #pygame.draw.line(screen,(255,175,175),[0,pipe_top],[height,pipe_top],5)
    #pygame.draw.line(screen,(255,175,175),[pipe_pos[0],0],[pipe_pos[0],width],5)
    ##DRAW TRAP
    #pygame.draw.line(screen,(255,175,175),trap[0],trap[1],5)

    #pygame.draw.line(screen,(255,175,175),[pipe_pos[0]+w,0],[pipe_pos[0]+w,width],5)

    #update score
   




    ###reposition if pipe passes screen
    if upipe_pos[0] < 3:
        #pipe_passed=True
        upipe_pos[0]=width
        #upp=random.randint(upipe_pos[1]-100,upipe_pos[1]+100)
        pipe_pos[0]=width
        upipe_pos[1]=random.randint(-200,50)
    #screen.blit(upipe,upipe_pos)

    return pipe_top,pipe_bottom,pipe_left,pipe_right,trap


def game(genomes, config): 
    
    #BIRD POSITION
    x=300
    
    #gNUM= gNUM+1
    nets=[]
    ge=[]
    birds=[]
    
    
    #generation=generation+1
    for  _, g in genomes:
        net=neat.nn.FeedForwardNetwork.create(g,config)
        nets.append(net)
        birds.append(Bird(350))
        g.fitness=0
        ge.append(g)
    
    run =True
    
    while run:
        
        screen.fill((0,0,0))
        """
        #UPDATE SCORE
        if pipe_pos[0] < x:
           
           myscore +=1
        """
        ###POPULATION AND SCORE
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render(str(len(birds)), True, (255,250,176), (0,0,0))
        textRect = text.get_rect()  
        textRect.center = (50, 50)
        """
        gen = font.render("GENERATION:"+str(gen_num), True, (255,250,176), (0,0,0))
        genRect = gen.get_rect()  
        genRect.center = (200, 50)
        
        scorecard=font.render(str(gNUM),True,(255,255,176), (0,0,0))
        scorerect=scorecard.get_rect()
        scorerect.center=(400,50)
        
        """
        screen.blit(text,textRect)
        #screen.blit(gen,genRect)
        #screen.blit(scorecard,scorerect) 
        
        ###DRAW BIRDS
        for bird in birds:
            bird.draw(screen)
        
        ###DRAW AND MOVE PIPES
        pipe_top,pipe_bottom,pipe_left,pipe_right,trap=draw_pipes(screen)
        move_pipes()
        """
        if pipe_right>pipe_right-pipe_left:
            pipe_passed=True
        """
        for x,bird in enumerate(birds):

            """
            j=random.randint(0,2)
            if j== 0:
                bird.jump()
            else:
                bird.dec_jump()
            """
            if bird.x > pipe_left:
                if bird.x < pipe_right:
                    if bird.y > pipe_bottom-30 or bird.y < pipe_top+10 :#or (bird.y <= trap[0][1]+25 and bird.y >= trap[0][1]-25):
                        birds.pop(x)
                        nets.pop(x)
                        ge[x].fitness -=1
                        ge.pop(x)
                    elif bird.y < 10 or bird. y > height- 10:
                        birds.pop(x)
                        nets.pop(x)
                        ge[x].fitness -=5
                        ge.pop(x)
                        
      
            
        ###increate fitness for moving forward
        for g in ge:
            g.fitness+= 0.3
        
        
        for x, bird in enumerate(birds):
           
            output = nets[x].activate((bird.y,abs(bird.y-pipe_top),abs(bird.y-pipe_bottom)))
            if output[0] > 0.5:
                bird.jump()
            else :
                bird.dec_jump()

        
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if len(birds) <=0 :
            run = False
            break
        
        
        clock.tick(20)
        pygame.display.flip()
    
    pipe_pos=[500,500]
    upipe_pos=[500,-100]
    #gen_num= gen_num+1
"""

what to do next?

set the jump trajectory
vary the pipe positions



"""





pygame.init()
width=500
height=500
screen=pygame.display.set_mode((width,height))

###GLOBAL VARIABLES

GAP=80
pipe_pos=[500,500]
upipe_pos=[500,-100]
gen_num=0

SCORE = 0
#p=100
jump_vel=5
x=300


GAP_BW_PIPES=500
pipe_passed=False


clock = pygame.time.Clock()


"""
###Create initial population
birds=[]
for i in range(p):
	bird=Bird(450)
	birds.append(bird)

"""

###NEAT 
local_dir=r'C:\Users\uic12963\Desktop\bharath\flappy bird'

config_path=os.path.join(local_dir,r'\Users\uic12963\Desktop\bharath\flappy bird\config-feedforward.txt')
config =neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                          neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
p=neat.Population(config)
p.add_reporter(neat.StdOutReporter(True))
p.add_reporter(neat.StatisticsReporter())

GENERATIONS=50
   
winner=p.run(game,GENERATIONS)
