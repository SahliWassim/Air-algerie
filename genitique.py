import numpy as np 
import random

def fitness(x,P):
    (n,m)=np.shape(P)
    f=0 
    for i in range(n):
         for j in range(m):
                f=f+x[i][j]*P[i][j]             
    return f
def croisement(x,y):
    (n,m)=np.shape(x)
    croisPoint=int(np.round(n/2))
    newX1=np.zeros((n,m))
    newX2=np.zeros((n,m))
    for i in range(croisPoint):
        for j in range(m):
            newX1[i][j]=x[i][j]
            newX2[i][j]=y[i][j]
    for i in range(croisPoint,n):
        for j in range(m):
            newX1[i][j]=y[i][j]
            newX2[i][j]=x[i][j]
    return newX1,newX2

def mutation(x):
    (n,m)=np.shape(x)
    rand_pilot = random.randint(0,n-1)
    rand_formation=random.randint(0,m-1)
    for j in range(m):
        x[rand_pilot][j]=0 
    x[rand_pilot,rand_formation]=1

def random_solution(W,C):
    (n, m) = np.shape(W)
    x=np.zeros((n,m))
    for i in range(n):
        rand_formation=random.randrange(m)
        x[i][rand_formation]=1
    fixSolution(x,W,C)
    return x

def init_pop(NPOP,P,W,C):
    POP=[]
    for k in range(NPOP):
        ind={"x":{},"f":{}}
        ind["x"]=random_solution(W,C)
        ind["f"]=fitness(ind["x"],P)
        POP.append(ind)
    POP= sorted(POP, key=lambda ind: ind['f'],reverse=True) 
    return POP

def selection(POP,NPOP):
    rand_x=random.randint(0,NPOP-1)
    rand_y=random.randint(0,NPOP-1)
    return POP[rand_x]["x"],POP[rand_y]["x"]
def isRealisable(x,W,c):
    (n,m)=np.shape(W)
    for i in range(n):
        w=0
        for j in range(m):
            w+=W[i][j]*x[i][j]
        if w > C[i]:
            return False
    return True
def fixSolution(x,W,C):
    (n,m)=np.shape(W)
    for i in range(n):
        w=0
        for j in range(m):
            w+=W[i][j]*x[i][j]
        while w>C[i]:
            for k in range(m):
                if x[i][k]==1:
                    x[i][k]=0
                    w-=W[i][k]
                    break
            break
def GA(P,W,C):
    (n,m)=np.shape(W)
    NPOP=100
    NITER=50
    MUTATION_RATE=0.01
    POP0=init_pop(NPOP,P,W,C)
    fancien=POP0[0]["f"]
    for i in range((NITER)):
        POP1=[]
        for k in range(int(NPOP/2)):
            #Selectionner deux parrents
            x,y=selection(POP0,NPOP)            
            x1,y1=croisement(x,y)
            r=np.random.rand()
            if r<MUTATION_RATE:
                mutation(x1)
                mutation(y1)
            fixSolution(x1,W,C)
            fixSolution(y1,W,C)
            POP1.append({"x":x1,"f":fitness(x1,P)})
            POP1.append({"x":y1,"f":fitness(y1,P)})
        allPOP= sorted(POP0+POP1, key=lambda ind: ind['f'],reverse=True) 
        POP0=allPOP[:NPOP]
        fbest=POP0[0]["f"]
        xbest=POP0[0]["x"]
        #print("Meilleure solution de la generation,{"+str(i)+"} :{"+str(fbest)+"}")
        
    return fancien,xbest,fbest