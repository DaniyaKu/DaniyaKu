import random
import numpy as np
from deap import creator, base, tools, algorithms
# решение задачи о рюкзаке (knapsack problem)
NUM_ITEMS = 50                    # число предметов
WEIGHT_LIMIT = 50               # максимальный вес рюкзака
VALUE = np.random.randint(1, 10, size=NUM_ITEMS)     # случайные значения предметов
WEIGHT = np.random.randint(1, 10, size=NUM_ITEMS)    # случайный вес предметов

# для задания хромосомы
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# для выборки, скрещивания и мутации индивидов
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, NUM_ITEMS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", lambda x: (sum([VALUE[i]*x[i] for i in range(len(x))]) if sum([WEIGHT[i]*x[i] for i in range(len(x))]) <= WEIGHT_LIMIT else 0,),)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# параметры генетического алгоритма
POP_SIZE = 50     # размер популяции
GEN_SIZE = 100     # число поколений
CROSS_PROB = 0.5    # вероятность скрещивания
MUT_PROB = 0.2    # вероятность мутации

# начальная популяция
pop = toolbox.population(n=POP_SIZE)

for gen in range(GEN_SIZE):
    offspring = algorithms.varAnd(pop, toolbox, CROSS_PROB, MUT_PROB)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for ind, fit in zip(offspring, fits):
        ind.fitness.values = fit
    pop = toolbox.select(offspring, k=len(pop))

# вывод лучшего индивида из популяции
best_ind = tools.selBest(pop, k=1)[0]
print("Лучший найденный набор предметов:", best_ind, "со значением функции цели", sum([VALUE[i]*best_ind[i] for i in range(len(best_ind))]), "и весом", sum([WEIGHT[i]*best_ind[i] for i in range(len(best_ind))]))