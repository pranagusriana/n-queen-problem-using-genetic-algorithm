import random
import math

class GeneticAlgorithmFunction:
    def __init__(self, n):
        self.n = n # N queen problem
        self.maxFitnessFunction = self.nCr(n, 2) # for N queen problem, fitness function refers to pair non attacking queen
    
    def replaceStr(self, str, pos, newstr):
        return str[:pos] + newstr + str[pos+1:]

    def nCr(self, n, r):
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

    def crossOver(self, parent1, parent2):
        # Assume len(parent1) == len(parent2)
        copoint = random.randrange(1, len(parent1)) # Random crossover point (1)
        child1 = ""
        child2 = ""
        for i in range(len(parent1)):
            if(i < copoint):
                child1 += parent1[i]
                child2 += parent2[i]
            else:
                child1 += parent2[i]
                child2 += parent1[i]
        # Choose best child between child1 and child2
        if(self.fitnessFunction(child1) > self.fitnessFunction(child2)):
            return child1
        else:
            return child2

    def mutation(self, chromosome):
        mutIdx = random.randrange(len(chromosome))
        return self.replaceStr(chromosome, mutIdx, str(random.randrange(1, self.n+1)))

    def reproduce(self, population, arrayOfFitness):
        newPopulation = []
        arrayOfProbdist = self.arrayOfProbdist(arrayOfFitness)
        for i in range(len(population)):
            parent1 = population[self.idxWheel(arrayOfProbdist)]
            parent2 = population[self.idxWheel(arrayOfProbdist)]
            child = self.crossOver(parent1, parent2)
            if(random.random() < random.random()):
                child = self.mutation(child)
            newPopulation += [child]
        return newPopulation

    def arrayOfFitnessFunction(self, population):
        ret = []
        for p in population:
            ret += [self.fitnessFunction(p)]
        return ret

    def arrayOfProbdist(self, arrayOfFitnessFunction):
        ret = []
        total = 0
        for ff in arrayOfFitnessFunction:
            total += ff
        for ff in arrayOfFitnessFunction:
            ret += [ff/total]
        return ret

    def idxWheel(self, arrayOfProbdist):
        lowerbound = 0
        upperbound = 0
        rn = random.random() # random number between 0 and 1
        for i in range(len(arrayOfProbdist)):
            upperbound += arrayOfProbdist[i]
            if(rn > lowerbound and rn <= upperbound):
                return i
            lowerbound = upperbound
    
    def fitnessFunction(self, chromosome):
        direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        coorChromosome = self.coorChromosome(chromosome)
        pairAttackingQueen = 0
        for i in range(len(chromosome) - 1):
            posMove = self.possibleMove(direction, coorChromosome[i])
            for j in range(i+1, len(chromosome)):
                if(coorChromosome[j] in posMove):
                    pairAttackingQueen += 1
        return self.maxFitnessFunction - pairAttackingQueen

    def coorChromosome(self, chromosome):
        coor = []
        for i in range(len(chromosome)):
            coor += [(self.n - int(chromosome[i]), i)]
        return coor

    def possibleMove(self, direction, coor):
        move = []
        for dir in direction:
            mul = 0
            coorMove = tuple(elmt1 + elmt2 for elmt1, elmt2 in zip(tuple(item * mul for item in dir), coor)) # mul * (d1, d2) + (c1, c2)
            while(coorMove[0] >= 0 and coorMove[0] < self.n and coorMove[1] >= 0 and coorMove[1] <= self.n):
                move += [coorMove]
                mul += 1
                coorMove = tuple(elmt1 + elmt2 for elmt1, elmt2 in zip(tuple(item * mul for item in dir), coor)) # mul * (d1, d2) + (c1, c2)
        return move

# Prana Gusriana
# 10 September 2021