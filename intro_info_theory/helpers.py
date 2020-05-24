import numpy as np
import scipy.stats

# return the entropy of distribution. expects dict of symboL:prob
def entropy(sym_prob: dict) -> float:
    return scipy.stats.entropy(list(sym_prob.values()), base=2)
