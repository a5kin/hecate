"""A collection of functions allowing genetics manipulations."""

from xentica import core
from xentica.tools import xmath


def genome_crossover(state, num_genes, *genomes, rng_name="rng"):
    """
    Crossover given genomes in stochastic way.

    :param state:
        A container holding model's properties.
    :param num_genes:
        Genome length, assuming all genomes has same number of genes.
    :param genomes:
        A list of genomes (integers) to crossover
    :param rng_name:
        Name of ``RandomProperty``.

    :returns: Single integer, a resulting genome.

    """
    gene_choose = core.IntegerVariable()
    new_genome = core.IntegerVariable()
    for gene in range(num_genes):
        gene_choose *= 0
        for i, genome in enumerate(genomes):
            gene_choose += ((genome >> gene) & 1) << i
        rand_val = getattr(state, rng_name).uniform
        winner_gene = xmath.int(rand_val * (len(genomes) + 1))
        new_genome += ((gene_choose >> winner_gene) & 1) << gene
    return new_genome
