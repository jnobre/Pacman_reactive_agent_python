
"""
iiaAgents.py

Created by Rui Lopes on 2012-02-18.
Copyright (c) 2012 University of Coimbra. All rights reserved.o
"""

from pacman import Directions, SCARED_TIME
from game import Agent
import random
import game
import util

class iiaPacmanAgent(Agent): 
    def getAction(self, state):
        """The agent receives a GameState (defined in pacman.py).
        Simple random choice agent. """
        return pacmania(self, state)

#verifica os campos de visao do pacman
def wall(x,y,direction,state):
    walls = state.getWalls()
    #print "Entra Wall Com=="
    #print direction
    
    #verifica as coordenadas excluindo atras
    if(direction==Directions.EAST):
        x=x+1   
        if walls[x][y]== False:
            return 0
        else:
            return -1
    elif(direction==Directions.WEST):
        x=x-1  
        if walls[x][y]== False:
            return 0
        else:
            return -1        
    elif(direction==Directions.NORTH):
        y=y+1
        if walls[x][y]== False:
            return 0
        else:
            return -1        
    elif(direction==Directions.SOUTH):
        y=y-1
        if walls[x][y]== False:
            return 0
        else:
            return -1                
    return 0
      
#sensor verifica se tem comida no campo de visao
def findfood(x,y,direction,state):
    
    px,py = state.getPacmanPosition()
    list_comida=state.getCapsules()    
    walls = state.getWalls()
    if(direction==Directions.EAST):
        x=x+1
        while walls[x][y]== False:
            if (state.hasFood(x,y)==True) or ((x,y) in list_comida):
                return -1
            else:
                x=x+1
    elif(direction==Directions.WEST):
        x=x-1
        while walls[x][y]== False:
            if (state.hasFood(x,y)==True) or ((x,y) in list_comida):
                return -1
            else:        
                x=x-1
                   
    elif(direction==Directions.NORTH):
        y=y+1
        while walls[x][y]== False:
            if (state.hasFood(x,y)==True) or ((x,y) in list_comida):
                return -1
            else:       
                y=y+1
          
    elif(direction==Directions.SOUTH):
        y=y-1
        while walls[x][y]== False:
            if (state.hasFood(x,y)==True) or ((x,y) in list_comida):
                return -1
            else:           
                y=y-1
    return 0

#sensor procura fantasma em determinada direcao
def findghost(x,y,direction,state,agent,num):
   
    #sensor guarda posicao dos fantasmas  e se ha parede
    posicoes=state.getGhostPositions()
    walls = state.getWalls()
    #se a direcao do pacman for este procura fantasma ate uma parede
    if (direction==Directions.EAST):
        x=x+1
        while walls[x][y]== False:    
            if(x,y) in posicoes:
                indice=posicoes.index((x,y))
                if state.getGhostState(indice+1).scaredTimer==0:
                    return -1
            x=x+1
    #se a direcao do pacman for oeste procura fantasma ate uma parede            
    elif(direction==Directions.WEST):
        x=x-1
        while walls[x][y]== False:
            if(x,y) in posicoes:
                indice=posicoes.index((x,y))
                if state.getGhostState(indice+1).scaredTimer==0:
                    return -1
            x=x-1
    #se a direcao do pacman for norte procura fantasma ate uma parede           
    elif(direction==Directions.NORTH):
        y=y+1
        while walls[x][y]== False:         
            if(x,y) in posicoes:
                indice=posicoes.index((x,y))
                if state.getGhostState(indice+1).scaredTimer==0:
                #print "Econtrou fantasma este"
                    return -1
            y=y+1
    #se a direcao do pacman for sul procura fantasma ate uma parede
    elif(direction==Directions.SOUTH):
        y=y-1
        while walls[x][y]== False:                            
            if(x,y) in posicoes:
                indice=posicoes.index((x,y))
                if state.getGhostState(indice+1).scaredTimer==0:
                #print "Econtrou fantasma este"
                    return -1
            y=y-1
    
    return 0

#sensor determina se ve fantasma e manda pacman para outra direcao     
def sensorpacman_escape(x,y,agent,state,direction,num):
    print "ENTRA SENSOR"
    #verifica as coordenadas para onde esta virado
    if(direction!=Directions.WEST):
        if (findghost(x,y,Directions.EAST,state,agent,num)==-1):
            #caso encontre fantasma escolhe uma direcao aleatoria, exluindo a direcao do fantasma e stop
            legal=state.getLegalActions(agent.index)
            legal.remove(Directions.EAST)
            if ((Directions.STOP in legal) and (len(state.getLegalActions(agent.index))>2)):
                legal.remove(Directions.STOP)
            escolha=random.choice(legal)
            return escolha
        
    if(direction!=Directions.EAST):
        if (findghost(x,y,Directions.WEST,state,agent,num)==-1):
            #caso encontre fantasma escolhe uma direcao aleatoria, exluindo a direcao do fantasma e stop
            legal=state.getLegalActions(agent.index)
            legal.remove(Directions.WEST)
            if ((Directions.STOP in legal) and (len(state.getLegalActions(agent.index))>2)):
                legal.remove(Directions.STOP)
            escolha=random.choice(legal) 
            return escolha
        
    if(direction!=Directions.SOUTH):
        if (findghost(x,y,Directions.NORTH,state,agent,num)==-1):
            #caso encontre fantasma escolhe uma direcao aleatoria, exluindo a direcao do fantasma e stop
            legal=state.getLegalActions(agent.index)
            legal.remove(Directions.NORTH)
            if ((Directions.STOP in legal) and (len(state.getLegalActions(agent.index))>2)):
                legal.remove(Directions.STOP)
            escolha=random.choice(legal)   
            #print escolha            
            return escolha
        
    if(direction!=Directions.NORTH):
        if (findghost(x,y,Directions.SOUTH,state,agent,num)==-1):
            #caso encontre fantasma escolhe uma direcao aleatoria, exluindo a direcao do fantasma e stop
            legal=state.getLegalActions(agent.index)
            legal.remove(Directions.SOUTH)
            if ((Directions.STOP in legal) and (len(state.getLegalActions(agent.index))>2)):
                legal.remove(Directions.STOP)
            escolha=random.choice(legal)  
            #print escolha
            return escolha

    return -1      

def pacmania(agent,state):
    print "PACMANIA"
    #guarda estado do pacman, bem como a sua direcao e suas posicoes
    teste=state.getPacmanState()
    direction=teste.getDirection()  
    x,y=(teste.getPosition())
    x=int(x);
    y=int(y);  
    
   
    #fantasma pode comer pacman, neste caso pacman tenta fugir se avistar fantasma
    num=state.getNumAgents() 
    if num > 1:   
        #encontra fantasma na direcao
        if(direction!=Directions.WEST):
            dir_esc=sensorpacman_escape(x,y,agent,state,Directions.EAST,num)
            if (dir_esc!=-1): 
                return dir_esc
                        
        if(direction!=Directions.EAST):
            dir_esc=sensorpacman_escape(x,y,agent,state,Directions.WEST,num)
            if (dir_esc!=-1):
                return dir_esc
                        
        if(direction!=Directions.SOUTH):
            dir_esc=sensorpacman_escape(x,y,agent,state,Directions.NORTH,num)
            if (dir_esc!=-1):
                return dir_esc
                        
        if(direction!=Directions.NORTH):
            dir_esc=sensorpacman_escape(x,y,agent,state,Directions.SOUTH,num)
            if (dir_esc!=-1):
                return dir_esc  
            
          
    #procura comida 
    if(direction!=Directions.WEST):
        if (findfood(x,y,Directions.EAST,state)==-1) and (Directions.EAST in state.getLegalActions(agent.index)):
            print("RETORNA ESTE")
            return Directions.EAST
            
    if(direction!=Directions.EAST):
        if (findfood(x,y,Directions.WEST,state)==-1) and (Directions.WEST in state.getLegalActions(agent.index)):
            print("RETORNA OESTE")
            return Directions.WEST
            
    if(direction!=Directions.SOUTH):
        if (findfood(x,y,Directions.NORTH,state)==-1) and (Directions.NORTH in state.getLegalActions(agent.index)):
            print("RETORNA NORTE")
            return Directions.NORTH
           
    if(direction!=Directions.NORTH):
        if (findfood(x,y,Directions.SOUTH,state)==-1) and (Directions.SOUTH in state.getLegalActions(agent.index)):
            print("RETORNA SUL")
            return Directions.SOUTH
        
    #Se nao encontrar comida
    if direction==Directions.NORTH:
        legal=state.getLegalActions(agent.index)
        if len(state.getLegalActions(agent.index))>2:
            legal.remove(Directions.SOUTH)
        legal.remove(Directions.STOP)
        escolha=random.choice(state.getLegalActions(agent.index))
        return escolha
    elif direction==Directions.SOUTH:
        legal=state.getLegalActions(agent.index)
        if len(state.getLegalActions(agent.index))>2:        
            legal.remove(Directions.NORTH)
        legal.remove(Directions.STOP)
        escolha=random.choice(legal)       
        return escolha
    elif direction==Directions.WEST:
        legal=state.getLegalActions(agent.index)
        if len(state.getLegalActions(agent.index))>2:
            legal.remove(Directions.EAST)
        legal.remove(Directions.STOP)
        escolha=random.choice(legal)
        return escolha    
    elif direction==Directions.EAST:
        legal=state.getLegalActions(agent.index)
        if len(state.getLegalActions(agent.index))>2:
            legal.remove(Directions.WEST)
        legal.remove(Directions.STOP)
        escolha=random.choice(legal)
        return escolha
    else:
        escolha=random.choice(state.getLegalActions(agent.index))
        return escolha        

    

class iiaGhostAgent(Agent):     
    """Uses a strategy pattern to allow usage of different ghost behaviors in the game. 
  The strategy must receive an agent and a GameState as the arguments.
  To set the strategy through command line use:
  >>>pacman.py -g iiaGhostAgent --ghostArgs fnStrategy='fun1[;fun*]'
  example:
   python pacman.py -g iiaGhostAgent --ghostArgs fnStrategy='goweststrategy;defaultstrategy'
   or
   python pacman.py -g iiaGhostAgent --ghostArgs fnStrategy=goweststrategy;defaultstrategy
   depending on the version used
  You may add new arguments as long as you provide a proper constructor. """   
        
    def __init__(self, index, fnStrategy='crazystrategy'):
        self.index=index
        strategies = fnStrategy.split(';')
        print strategies
        try:
            self.strategy = util.lookup(strategies[index%len(strategies)], globals())
        except:
            print "Function "+strategies[index%len(strategies)]+" not defined!"
            print "Loading defaultstrategy..."
            self.strategy = defaultstrategy
      
    def getAction(self, state):
        """The agent receives a GameState (defined in pacman.py).
         Simple random ghost agent."""
        return self.strategy( self, state )  
 


#sensor procura pacman no campo de visao
def findpath(x,y,direction,state):
    px,py = state.getPacmanPosition()
    walls = state.getWalls()
    if (direction==Directions.EAST):
        x=x+1
        while walls[x][y]== False:       
            if((x == px) and (y == py)):
                return -1
            else:
                x=x+1
                
    elif(direction==Directions.WEST):
        x=x-1
        while walls[x][y]== False:
            if((x == px) and (y == py)):
                return -1
            else:
                x=x-1
                
    elif(direction==Directions.NORTH):
        y=y+1
        while walls[x][y]== False:        
            if((x == px) and (y == py)):
                return -1
            else:
                y=y+1
                
    elif(direction==Directions.SOUTH):
        y=y-1
        while walls[x][y]== False:         
            if((x == px) and (y == py)):
                return -1
            else:
                y=y-1
    
    return 0
 

#sensor se encontrar fantasma tenta fugir
def sensorghost_escape(x,y,agent,state,direction):

       
    if(direction!=Directions.WEST):
        if (findpath(x,y,Directions.EAST,state)==-1):
            #percorre todas as possibilidades
            for i in state.getLegalActions(agent.index):
                if(i != Directions.EAST):
                    return i;
        
        
    if(direction!=Directions.EAST):
        if (findpath(x,y,Directions.WEST,state)==-1):
            for i in state.getLegalActions(agent.index):
                if(i != Directions.WEST):
                    return i;
        
    if(direction!=Directions.SOUTH):
        if (findpath(x,y,Directions.NORTH,state)==-1):
            for i in state.getLegalActions(agent.index):
                if(i != Directions.NORTH):
                    return i;  
    
    if(direction!=Directions.NORTH):
        if (findpath(x,y,Directions.SOUTH,state)==-1):
            for i in state.getLegalActions(agent.index):
                if(i != Directions.SOUTH):
                    return i;  


    return random.choice(state.getLegalActions(agent.index))          

#funcao que define comportamente do fantasma o direto
def crazystrategy(agent,state):
  
    # Fantasma "O Directo"
    teste=state.getGhostState(agent.index)
    direction=teste.getDirection()

    x,y=(teste.getPosition())
    x=int(x)
    y=int(y)
    
    #pacman pode comer
    if(teste.scaredTimer>0):
        print state.getLegalActions(agent.index)
        #sensor para escapar do pacman 
        return sensorghost_escape(x,y,agent,state,direction)
    else:
      #a busca do pacman
        if(direction!=Directions.WEST):
            if (findpath(x,y,Directions.EAST,state)==-1) and (Directions.EAST in state.getLegalActions(agent.index)):
                return Directions.EAST
      
        if(direction!=Directions.EAST):
            if (findpath(x,y,Directions.WEST,state)==-1) and (Directions.WEST in state.getLegalActions(agent.index)):
                return Directions.WEST
      
        if(direction!=Directions.SOUTH):
            if (findpath(x,y,Directions.NORTH,state)==-1) and (Directions.NORTH in state.getLegalActions(agent.index)):
                return Directions.NORTH
      
        if(direction!=Directions.NORTH):
            if (findpath(x,y,Directions.SOUTH,state)==-1) and (Directions.SOUTH in state.getLegalActions(agent.index)):
                return Directions.SOUTH
      
    return random.choice(state.getLegalActions(agent.index))

def goweststrategy(agent,state):
    print "gowest"
    print state.getLegalActions(agent.index)
    if Directions.WEST in state.getLegalActions(agent.index):
        return Directions.WEST
    else:
        return random.choice(state.getLegalActions(agent.index))

#fantasmas medricas, primeiro procura companhia para apanhar o fantasma
def medricas(agent,state):
    #memoria controlador se existe fantasma no campo de visao
    see_ghost=-1
    teste=state.getGhostState(agent.index)
    direction=teste.getDirection()
    x,y=(teste.getPosition())
    x=int(x)
    y=int(y)
    #memoria
    num=state.getNumAgents()
    if(teste.scaredTimer>0):
        print state.getLegalActions(agent.index)
        #sensor para escapar do pacman 
        return sensorghost_escape(x,y,agent,state,direction)
    else:
        #print "direacao ................."
       # print direction
        
        #procura outro fantasma
        if(direction!=Directions.WEST):
            if (findghost(x,y,Directions.EAST,state,agent,num)!=-1):
                see_ghost=1
                if Directions.EAST in state.getLegalActions(agent.index):
                    return Directions.EAST
                        
        if(direction!=Directions.EAST):
            if (findghost(x,y,Directions.WEST,state,agent,num)!=-1):
                see_ghost=1
                if Directions.WEST in state.getLegalActions(agent.index):
                    return Directions.WEST                
                        
        if(direction!=Directions.SOUTH):
            if (findghost(x,y,Directions.NORTH,state,agent,num)!=-1):
                if Directions.NORTH in state.getLegalActions(agent.index):
                    return Directions.NORTH
                        
        if(direction!=Directions.NORTH):
            if (findghost(x,y,Directions.SOUTH,state,agent,num)==-1):
                see_ghost=1
                if Directions.SOUTH in state.getLegalActions(agent.index):
                    return Directions.SOUTH                
                
        #se encontrar procura pacman
        if see_ghost==1:
            if(direction!=Directions.WEST):
                if (findpath(x,y,Directions.EAST,state)==-1) and (Directions.EAST in state.getLegalActions(agent.index)):
                    return Directions.EAST
                
            if(direction!=Directions.EAST):
                if (findpath(x,y,Directions.WEST,state)==-1) and (Directions.WEST in state.getLegalActions(agent.index)):
                    return Directions.WEST
                
            if(direction!=Directions.SOUTH):
                if (findpath(x,y,Directions.NORTH,state)==-1) and (Directions.NORTH in state.getLegalActions(agent.index)):
                        return Directions.NORTH
                     
            if(direction!=Directions.NORTH):
                if (findpath(x,y,Directions.SOUTH,state)==-1) and (Directions.SOUTH in state.getLegalActions(agent.index)):
                    return Directions.SOUTH  
                  
    print state.getLegalActions(agent.index)
    return random.choice(state.getLegalActions(agent.index))