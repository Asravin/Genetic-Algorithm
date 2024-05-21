from random import randint

class Chromosome:
    def __init__(self, size, gene_pool):
        self.rating = 0
        self.size = size
        self.genes = bytearray(size)
        if gene_pool is not None:
            self.set_random_genes(gene_pool)
    
    
    def set_random_genes(self, gene_pool):
        gene_pool_range = len(gene_pool) - 1
        for i in range(self.size):
            rand_pos = randint(0, gene_pool_range)
            self.genes[i] = gene_pool(rand_pos)
            
    
    def create_population(pop_size, chromo_size, genes):
        population = [None] * pop_size
        for i in range(pop_size):
            population[i] = Chromosome(chromo_size, genes)
        return population
    
    
    def calc_rating(population, final_chromo):
        for chromo in population:
            chromo.rating = chromo.size
            for i in range(chromo.size):
                if chromo.genes[i] == final_chromo:
                    chromo.rating -= 1
    
    
    def sort_population(population):
        size = len(population)
        repeat = True
        while repeat:
            repeat = False
            for i in range(0, size - 1):
                bubble =population[i]
                if(bubble.rating > population[i + 1].rating):
                    population[i] = population[i + 1]
                    population[i + 1] = bubble
                    repeat = True
                
            
               
            