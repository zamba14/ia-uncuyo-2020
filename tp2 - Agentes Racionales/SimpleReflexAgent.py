
import numpy as np


class Environment:

    def __init__(self, sizeX,sizeY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirt_rate = dirt_rate
        self.board = np.random.choice(a=[True,False], size=(self.sizeX, self.sizeY), p=[dirt_rate, 1-dirt_rate])
      
    def clean(self, agent):
        self.board[agent.y][agent.x] = False
        return True
    
    def is_dirty(self, agent):
        return self.board[agent.y][agent.x]

    def print_environment(self, ag):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                placeholder = ""
                if self.board[y][x]:
                    if ag.x==x and ag.y==y:
                        placeholder = "-T-"
                    else:
                        placeholder = " T "
                else:
                    if ag.x==x and ag.y==y:
                        placeholder = "-F-"
                    else:
                        placeholder = " F "
                print("[",placeholder,"]", end=" ")
            print("")

class SimpleReflexAgent:
    #Simple reflex agent. If it has dirt right in front of it, it will clean it. Otherwise, will pick a random possible action.
    #Will work until no cycles left or all dirt has been cleaned.
    def __init__(self, env):
        self.env = env
        self.x = np.random.randint(0,env.sizeX)
        self.y = np.random.randint(0,env.sizeY)
        self.cycles = 1000
        self.performance = 0
    def print_agent(self):
        print("agent y: %d x: %d cycles left: %d dirt left: %s performance: %d" %(self.y,self.x, self.cycles, self.goal(), self.performance))
    def goal(self):
        return self.env.board.any()
    def clean(self, look):
        if self.env.is_dirty(self):
            if (look):
                return True
            else:
                self.env.clean(self)
                self.cycles-=1
                self.performance +=1
                print("cleaned y: %d x: %d" % (self.y,self.x))
        else:
            return False
    def move_up(self, look):
        if self.y > 0:
            if(look):
                
                return True
            else:
                self.y-=1
                self.cycles-=1
                print("move up")
        else:
            return False
    def move_down(self, look):
        if self.y < self.env.sizeY-1:
            if(look):
                return True
            else:
                self.y+=1
                self.cycles-=1
                print("move down")
        else:
            return False
    def move_left(self, look):
        if self.x > 0:
            if(look):
                
                return True
            else:
                self.x-=1
                self.cycles-=1
                print("move left")
        else:
            return False
    def move_right(self, look):
        if self.x < self.env.sizeX-1:
            if(look):
                
                return True
            else:
                self.x+=1
                self.cycles-=1
                print("move right")
        else:
            return False
    def idle(self):
        pass
    def perspective(self):
        possible_actions = [self.move_up, self.move_down, self.move_left, self.move_right, self.clean]
        actions = []
        for action in possible_actions:
            if(action(look=True)):
                actions.append(action)
        return actions
    def get_action(self, name):
        actions = [self.move_up, self.move_down, self.move_left, self.move_right, self.clean]
        for action in actions:
            if action.__name__ == name:
                return action
    def report(self):
        for action in self.perspective():
            print(action.__name__, end=" ")
        self.print_agent()
    def think(self):
        #Strategy: get a corner and then swipe everything
        cornersX = ["move_left","move_right"]
        cornersY = ["move_up", "move_down"]
        directionX = 0 if self.x < self.env.sizeX/2 else 1
        directionY = 0 if self.y < self.env.sizeY/2 else 1
        actions = [self.get_action(cornersX[directionX])]*abs(self.x-(self.env.sizeX-1 if self.x > self.env.sizeX/2 else 0 ))
        actions.extend([self.get_action(cornersY[directionY])]*abs(self.y-(self.env.sizeY-1 if self.y > self.env.sizeY/2 else 0)))
        for action in actions:
            print(action.__name__)
            action(look=False)
        #Now i'm in the corner
        #Invert directions
        directionX = abs(directionX - 1)
        directionY = abs(directionY - 1)
        path = [self.get_action(cornersY[directionY])]*abs(self.env.sizeY)
        
        for row in path:
            columns = [self.get_action(cornersX[directionX])]*(self.env.sizeX-1)
            for column in columns:
                self.clean(look=False)
                column(look=False)
            directionX = abs(directionX - 1)
            self.clean(look=False)
            row(look=False)
            

    def work(self):
        pass

env = Environment(16,16,0.8)
ag = SimpleReflexAgent(env)
ag.print_agent()
env.print_environment(ag)
ag.think()
ag.print_agent()
env.print_environment(ag)



