import math

import networkx
import networkx as nx
import numpy as np
import dwave_networkx as dnx
import networkx.algorithms.approximation as nx_app
from matplotlib import pyplot as plt
from itertools import chain, combinations

"""
Minimum Vertex Cover Algorithm

The algorithm returns an approximate minimum weighted vertex cover.
The set of nodes returned by this function is guaranteed to be a vertex cover,
and the total weight of the set is guaranteed to be at most twice the total
weight of the minimum weight vertex cover. In other words, w(s) <= 2*w(s*)
"""




def power_set(n):
    return chain.from_iterable(combinations(range(n), r) for r in range(n + 1))


def min_vertex_cover(G: networkx.classes.graph.Graph):
    """
    The func returns a minimum weighted vertex cover and its weight.
    The func use in a simple and inefficient algorithm.
    """
    cover_sets = power_set(G.number_of_nodes())
    min_weight = math.inf
    min_set = None
    for set in cover_sets:
        if dnx.is_vertex_cover(G, set):
            curr_weight = sum([G.nodes[n]['weight'] for n in set])
            if curr_weight < min_weight:
                min_weight = curr_weight
                min_set = set
    return min_set, min_weight


def approximate_min_vertex_cover(G: networkx.classes.graph.Graph):
    """
    The func returns an approximate minimum weighted vertex cover and its weight.
    The func use in the networkx approximation algorithm.
    """
    min_set = nx_app.min_weighted_vertex_cover(G)
    min_weight = sum([G.nodes[n]['weight'] for n in min_set])
    return min_set, min_weight


def print_graph(G):
    for n, w in G.nodes.data('weight'):
        print(f'node = {n} , weight = {w:.3}')


def random_weighted_graph(num_of_nodes, probability_of_edge):
    G = nx.gnp_random_graph(num_of_nodes, probability_of_edge)
    for s in G.nodes:
        G.nodes[s]['weight'] = np.random.random()
    return G


def my_plot():
    prob = [0.2, 0.4, 0.6, 0.8]
    size = [s for s in range(5, 21)]
    f, ax = plt.subplots(1, 4, sharex='col', sharey='row', figsize=(20, 10))

    for i, p in enumerate(prob):
        # list_algo = []
        # list_approximate_algo = []
        approximation_ratio = []
        for s in size:
            print(s)
            G = random_weighted_graph(s, p)
            # list_algo.append(min_vertex_cover(G)[1])
            # list_approximate_algo.append(approximate_min_vertex_cover(G)[1])
            approximation_ratio.append((approximate_min_vertex_cover(G)[1]) / (min_vertex_cover(G)[1]))

        ax[i].set_title(f"P = {p}")
        ax[i].plot(size, approximation_ratio)

    plt.show()


if __name__ == '__main__':
    my_plot()
