import numpy as np
class Board():
    def __init__(self, board, size):
        self.board = board
        self.size = size
    def print(self):
        print(self.board)
    def fitness(self):
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

def num(size):
    return np.random.randint(0,size)

def genetic_algoritm(pop_number, board_size, max_generations):
    population = initialize_population(pop_number, board_size)
    solution = False
    generations = 0
    while (not solution and generations<max_generations):
        population_fitness = []
        generations +=1
        print("generation ", generations)
        for board in population:
            fitness = 100 - board.fitness()
            population_fitness.append(fitness)
            print(board.board,fitness)
            if fitness == 100:
             solution = True
             return board.board, generations
        fitness_sum = sum(population_fitness)
        population_selection = np.random.choice(population,p= [a/fitness_sum for a in population_fitness], size= pop_number//2)
        population = crossOver(population_selection)
        mutation(population,board_size)
        
        #input("press Enter")
        
def crossOver(population):
    new_population = []
    for i in range(len(population)//2):
        father = population[i].board
        mother = population[len(population)-(i+1)].board
        punto_cruce = np.random.randint(0,len(father))
        offspring1 = father[0:punto_cruce]+mother[punto_cruce:]
        offspring2= mother[0:punto_cruce]+father[punto_cruce:]
        new_population.append(Board(offspring1,len(father)))
        new_population.append(Board(offspring2, len(father)))
    return new_population

def mutation(population, board_size):
    for board in population:
        if(np.random.choice([True,False])):
            random_index = (np.random.randint(0,board_size))
            random_value = (np.random.randint(0,board_size))
            board.board[random_index] = random_value


def initialize_population(pop_number, board_size):
    population = []
    for _ in range(pop_number):
        board = Board([num(board_size) for i in range(board_size)],board_size)
        population.append(board)
    return population

print(genetic_algoritm(100,8,100))
    


