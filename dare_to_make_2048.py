"""Welcome MOHASIN HAQUE You started this on 23/December/2020 this will be short but quite tough but hope
You will finsh it.
You finished it at 31/December/2020 (This Program does not depend on any assist File.)
You take a help from another programmer to prepare algorithm
"""
"""WHERE ALL MEN BLINDLY FOLLOW THE TRUTH
 REMEMBER....NOTHING IS TRUE
WHERE ALL MEN ARE LIMITED BY MORTAILITY OR LAW
 REMEMBER.....EVERYTHING IS PERMITTED
 WE WORK IN THE DARK SO THAT LIGHT MAY EXIST..................................."""
from pygame import key,event
import pygame, sys
from pygame.locals import *
import pygame.locals


pygame.init()
fpsClock = pygame.time.Clock()
SIZE = 4
BLOCKSIZE=100
MAX=SIZE*BLOCKSIZE
_GameEnd=None #Variable that will control game run
_GameOver=None
color=pygame.Color
windowSurfaceObj = pygame.display.set_mode((MAX,MAX+100)) #win in my other projects
pygame.display.set_caption('DARE TO MAKE 2048')
lighterblue = color(235,255,255)
grey = color(145,141,142)
gold = color(255,215,0)
black= color(0,0,0)
granite = color(131,126,124) #initializing colors
box1 = color(201,196,194)


redColor = color(255,255,0)
greenColor = color(0,255,0)
blueColor = color(0,0,255)
whiteColor = color(255,255,255)
lightblue = color(173, 216, 230)


mousex,mousey = 0,0
fon = pygame.font.SysFont('verdana',25)
text=fon.render('     By MOHASIN HAQUE \n ',1,(0,0,0))
fontObj = pygame.font.SysFont('verdana',32)
fontObj2 = pygame.font.SysFont('verdana',32)
fontObj16 = pygame.font.SysFont('verdana',28)
fontObj128 = pygame.font.SysFont('verdana',26,bold=True)
fontObj1024 = pygame.font.SysFont('verdana',24,bold=True)
fontObj16384 = pygame.font.SysFont('verdana',23,bold=True)
fontObjSmall = pygame.font.SysFont('verdana',22,bold=True)


fonts =[fontObj2,fontObj16,fontObj128,fontObj1024,fontObj16384,fontObjSmall]
color2 =(229,228,227)
color4 = pygame.Color(229,182,147)
colors = {2:(229,228,227),4:(229,228-20,227-40),8:(229,228-30,227-60),16:(229,150,100),
       32:(200,100,50),64:(150,60,30),128:(255,219,90),
       256:(229,200,70),512:(229,180,50),1024:(229,170,40),2048:(229,160,20),
       4096:(0,0,0),8192:(0,0,100),16384:(30,0,0),32768:(60,0,0)}
lineArray = []
for a in range(BLOCKSIZE,MAX,BLOCKSIZE) :
 lineArray.append( (0,a))
 lineArray.append((MAX,a))
 lineArray.append((MAX,a+BLOCKSIZE))
lineArray.append((MAX,0))
lineArray.append((0,0))
for a in range(BLOCKSIZE,MAX,BLOCKSIZE) :
 lineArray.append( (a,0))
 lineArray.append((a,MAX))
 lineArray.append((a+BLOCKSIZE,400))

 
def processMovement(myList:list,directive:int):
     

 newList=[]
 Matrix = [[0 for x in range(SIZE)] for x in range(SIZE)]
 for (x,y,z) in myList:
   Matrix[y//BLOCKSIZE][x//BLOCKSIZE]=z
 if directive == pygame.K_DOWN: # 90 rotation
    Matrix=[list(elem) for elem in zip(*Matrix[::-1])]
    Matrix,score=addMatrix(Matrix)
    Matrix=[list(elem[::-1]) for elem in zip(*Matrix[::-1])][::-1]
 if directive == pygame.K_UP:
    Matrix=[list(elem) for elem in zip(*Matrix)]
    Matrix,score=addMatrix(Matrix)
    Matrix=[list(elem) for elem in zip(*Matrix)]
    
 elif directive == pygame.K_LEFT: # no rotation
    Matrix,score=addMatrix(Matrix)
    
 elif directive == pygame.K_RIGHT: # 180 rotation
    Matrix=[each [::-1] for each in Matrix[::-1]]
    Matrix,score=addMatrix(Matrix)
    Matrix=[each [::-1] for each in Matrix[::-1]]

    
 for j,line in enumerate(Matrix):
    for i,each in enumerate(line):
      if each!=0:
          newList.append([i*BLOCKSIZE,j*BLOCKSIZE,each])
 standStill = True if sorted(myList)==sorted(newList) else False

 
 return newList,standStill,score

def addMatrix(myList:list):
 newList=[]
 newLine=[]
 score=0
 lastPaired=False
 for i,line in enumerate(myList):
    for i,each in enumerate(line):

      if each ==0:
        pass
      elif len(newLine)>0 and newLine[-1]==each and not lastPaired:
        newLine[-1]= 2*int(each)
        score=score+2*int(each)
        lastPaired=True
        if each==1048 and _GameEnd==None : _GameEnd=True
      else:
        lastPaired=False
        newLine.append(int(each))
    lastPaired=False
    newLine.extend( [0] *(SIZE-len(newLine)))

    newList.append(newLine)
    newLine=[]
 return newList,score
def getRandBox(myList):
  simpleLock=[]
  simpleEmpty=[]
  for [x,y,z] in myList:
    simpleLock.append((y//100)*4+x//100)
  simpleEmpty=[x for x in range(0,16) if x not in simpleLock]
  import random
  x=random.choice(simpleEmpty)
  z = random.randint(0,10)
  z = 2 if z <= 9 else 4
  return [(x%4)*100,(x//4)*100,z]
def drawBox(box,border=None):
 x,y,z=box
 if(border==None):
   border= color2
 fillColor=colors[z if z<32768 else -1 ]
 myRect=pygame.draw.rect(windowSurfaceObj,border,(x+2,y+2,98,98),0)
 windowSurfaceObj.fill(border,myRect)
 windowSurfaceObj.fill(fillColor, myRect.inflate(-5, -5))
 msg=str(z)
 msgSurfaceObj = fontObj.render(msg,True,granite if z<16 else whiteColor)
 msgRectobj = msgSurfaceObj.get_rect()
 msgRectobj.center = (x+50,y+52)
 windowSurfaceObj.blit(msgSurfaceObj,msgRectobj)
locked=[]
new = (getRandBox(locked))
locked.append(new)
action = None
Total = 0
def run_game():
 windowSurfaceObj.blit(text,(0,MAX))
 pygame.display.update()
 fpsClock.tick(30)
while True:
 windowSurfaceObj.fill(lightblue)
 pygame.draw.lines(windowSurfaceObj,lighterblue,False,lineArray,2)
 if len(locked)==1:
   drawBox(locked[-1],gold)
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   elif event.type == pygame.MOUSEMOTION:
     mousex, mousey = event.pos
 #soundObj.play()
   elif event.type == pygame.KEYDOWN:
    if event.key in (pygame.K_LEFT,pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
       standStill=False
       action = event.key
       locked,standStill,score=processMovement(locked,event.key)
       if not standStill:
          Total = Total + score
          new =getRandBox(locked) #get random box
          locked.append(new) #append to locked
          if(len(locked)==SIZE*SIZE):
              _,standStill1,_=processMovement(locked,pygame.K_RIGHT)
              _,standStill2,_=processMovement(locked,pygame.K_LEFT)
              _,standStill3,_=processMovement(locked,pygame.K_UP)
              _,standStill4,_=processMovement(locked,pygame.K_DOWN)
              _GameOver = standStill1 or standStill2 or standStill3 or standStill4
       if event.key == pygame.K_a:
          msg = "'A'Key pressed"
       if event.key == pygame.K_ESCAPE:
           pygame.event.post(pygame.event.Event(pygame.QUIT))
    if action:
      for i in locked[:-1]:
        drawBox(i,grey)
      drawBox(locked[-1],gold)
    run_game()
#Finally it is working don't touch it now 
