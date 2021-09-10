from GeneticAlgorithmFunction import GeneticAlgorithmFunction
import random
import time

class NQueenSolver:
    def __init__(self, n):
        self.n = n
        self.gaFunction = GeneticAlgorithmFunction(n) # Genetic Algorithm Function Object

    def createRandomChromosome(self):
        chromosome = ""
        for i in range(self.n):
            chromosome += str(random.randrange(1, self.n+1))
        return chromosome

    def createRandomPopulation(self, sizePopulation):
        population = []
        for i in range(sizePopulation):
            population += [self.createRandomChromosome()]
        return population

    def printChromosome(self, chromosome):
        coorChromosome = self.gaFunction.coorChromosome(chromosome)
        sret = ""
        for i in range(len(chromosome)):
            for j in range(len(chromosome)):
                if((i, j) in coorChromosome):
                    sret += "Q".center(4)
                else:
                    sret += "x".center(4)
            sret += "\n"
        print(sret)

    def solve(self, sizePopulation):
        if(self.n > 2):
            start = time.time()
            population = self.createRandomPopulation(sizePopulation)
            print("INITIAL POPULATION".center(4 * self.n, "-"))
            arff = self.gaFunction.arrayOfFitnessFunction(population)
            generation = 0
            for p in range(len(population)):
                print(population[p], f", Fitness Function = {arff[p]}")
                self.printChromosome(population[p])
            while(not(self.gaFunction.maxFitnessFunction in arff)):
                population = self.gaFunction.reproduce(population, arff)
                arff = self.gaFunction.arrayOfFitnessFunction(population)
                generation += 1
            for i in range(len(arff)):
                if(arff[i] == self.gaFunction.maxFitnessFunction):
                    print("SOLUTION".center(4 * self.n, "-"))
                    print(f"{population[i]}, Solution found at {generation} generations")
                    self.printChromosome(population[i])
                    print(f"{self.n} Queens Problem using genetic algorithm finished in {time.time() - start} seconds")
                    break
        else:
            print("No solution for n <= 2")

if __name__ == "__main__":
    N = int(input("Enter Number of Queens: "))
    NQueenSolver(N).solve(10) # Solve N Queens Problem using genetic algorithm  with population size = 10

# Prana Gusriana
# 10 September 2021