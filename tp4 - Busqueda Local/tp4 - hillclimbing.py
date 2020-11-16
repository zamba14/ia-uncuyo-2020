import numpy as np
from queue import PriorityQueue
class Board():
    def __init__(self, board, size):
        self.board = board
        self.size = size
    def print(self):
        print(self.board)
    def h(self):
        h_value = 0
        diag_up = [sum (x) for x in zip(self.board,[i for i in range(self.size)])]
        diag_down = [sum (x) for x in zip([-i for i in range(self.size)], self.board)]
        for i in range(self.size*2):
            for j in range(self.board.count(i)):
                h_value += j
        for i in range(self.size*2):
            for j in range(diag_up.count(i)):
                
                h_value += j
            for x in range(diag_down.count(i)):
                
                h_value+=x
            for z in range(diag_down.count(-i)):
                
                h_value+=z
            
        return h_value
    def make_neighbors(self):
        neigbors = PriorityQueue()
        count = 0
        
        for i in range(self.size):
            for j in range(self.size):
                new_board = self.board.copy()
                if (j != new_board[i]):
                    count += 1
                    new_board[i] = j
                    this_board = Board(new_board, self.size)
                    neigbors.put((this_board.h(),count,this_board))
        return neigbors

def num(size):
    return np.random.randint(0,size)

def hill_climbing(board, loops):
    current_board = board
    solution = False
    current_loops = 0

    while (not solution and current_loops < loops):
        current_h_score = current_board.h()
        neighbor = current_board.make_neighbors().get()
        neighbor_h_score = neighbor[0]
        neighbor_board = neighbor[2]
        current_loops +=1

        if (neighbor_h_score < current_h_score):
            current_board = neighbor_board
        else:
            solution = True
            print("loops: ", current_loops)
        
    return current_board

def run_algoritm():
    board = Board([num(8) for i in range(8)],8)
    board.print()
    solution = hill_climbing(board,1000)
    solution.print()
    print(solution.h())

for i in range(30):
    print("run ", i+1)
    run_algoritm()



