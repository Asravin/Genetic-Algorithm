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
            
            