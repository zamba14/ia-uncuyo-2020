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
        neigbors = []
        count = 0
        
        for i in range(self.size):
            for j in range(self.size):
                new_board = self.board.copy()
                if (j != new_board[i]):
                    count += 1
                    new_board[i] = j
                    this_board = Board(new_board, self.size)
                    neigbors.append(this_board)
        return neigbors

def num(size):
    return np.random.randint(0,size)

def simulated_annealing(board, loops):
    current_board = board
    solution = False
    current_loops = loops

    while (not solution and current_loops > 1):
        current_h_score = current_board.h()
        neighbor = np.random.choice(current_board.make_neighbors())
        neighbor_h_score = neighbor.h()
        current_loops -=1
        delta_e = neighbor_h_score - current_h_score

        if (delta_e < 0):
            current_board = neighbor
        else:
            chosen_board = np.random.choice([current_board, neighbor], p=[1-current_loops/loops,current_loops/loops])
            current_board = chosen_board
    print("loops ",loops-current_loops)
    return current_board
def run_algoritm():
    board = Board([num(8) for i in range(8)],8)
    solution = simulated_annealing(board,1000)
    print(solution.h())
    board.print()
    solution.print()

for i in range(30):
    print("run ",i+1)
    run_algoritm()
    
