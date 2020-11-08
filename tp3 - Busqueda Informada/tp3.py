import numpy as np
from queue import PriorityQueue
from termcolor import colored, cprint
import colorama
import os

class Node:
    def __init__ (self, y, x, total_rows):
        self.x = x
        self.y = y
        self.type = "white"
        self.total_rows = total_rows
        self.neighbors = []
    #GET PROP
    def get_pos(self):
        return self.y, self.x
    def is_closed(self):
        return self.type == "grey"
    def is_open(self):
        return self.type == "white"
    def is_barrier(self):
        return self.type =="red"
    def is_start (self):
        return self.type =="magenta"
    def is_end (self):
        return self.type == "yellow"
    def get_neighbors(self,grid):
        self.neighbors = []
        if self.y < self.total_rows-1 and not grid[self.y+1][self.x].is_barrier():
            self.neighbors.append(grid[self.y+1][self.x])
        if self.y > 0 and not grid[self.y-1][self.x].is_barrier():
            self.neighbors.append(grid[self.y-1][self.x])
        if self.x < self.total_rows-1 and not grid[self.y][self.x+1].is_barrier():
            self.neighbors.append(grid[self.y][self.x+1])
        if self.x > 0 and not grid[self.y][self.x-1].is_barrier():
            self.neighbors.append(grid[self.y][self.x-1])
    #SET PROP
    def make_closed(self):
        self.type = "grey"
    def make_open(self):
        self.type = "white"
    def make_barrier(self):
        self.type ="red"
    def make_start (self):
        self.type ="magenta"
        return self
    def make_end (self):
        self.type = "yellow"
        return self
    def make_path(self):
        self.type = "green"
    def draw(self):
        #text = colored("██", self.type)
        #print(text, end="")
        cprint("██", self.type, end="")

def h(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def aStar(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        current_node = open_set.get()[2]
        open_set_hash.remove(current_node)

        if current_node == end:
            make_path(came_from, end)
            end.make_end()
            start.make_start()
            break
        current_node.get_neighbors(grid)
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node]+1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count +=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        current_node.make_closed()



def make_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        print(current.get_pos())

def make_grid(rows):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i,j, rows)
            grid[i].append(spot)
    return grid

def print_grid(grid):
    for row in grid:
        for spot in row:
            spot.draw()
        print("")

def make_obstacules(grid, rows):
    for i in range(rows*5):
        i = np.random.randint(0,rows)
        j = np.random.randint(0,rows)
        grid[i][j].make_barrier()
    s1 = np.random.randint(0,rows)
    s2 = np.random.randint(0,rows)
    start = grid[s1][s2].make_start()
    e1 = np.random.randint(0,rows)
    e2 = np.random.randint(0,rows)
    end = grid[e1][e2].make_end()
    return start, end
def take_all_neighbors(grid):
    for row in grid:
        for spot in row:
            spot.get_neighbors(grid)


colorama.init()
grid_size = 50
grid = make_grid(grid_size)
start, end = make_obstacules(grid, grid_size)
print_grid(grid)
#take_all_neighbors(grid)
print("START NODE = ",start.get_pos())
print("END NODE = ",end.get_pos())

aStar(grid,start,end)
print_grid(grid)
input("press Enter to finish")