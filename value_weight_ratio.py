#coding: utf-8

"""Calculate the value/weight ratio for each item
Choose items from the highest ratio to the lowest ratio until total weight reaches limited capcaity"""


def value_weight_ratio(capacity, treasures):
    """capacity: the capacity of knapsack
    treasures: lists of tuples like (weight,value)
    return: tuple like: (best cost, best selection of items: list of 1 and 0)
    """
    ratios = [(index, item[1] / float(item[0])) for index, item1 in enumerate(treasures)]
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)
    best_subset = [0] * len(treasures[0])
    best_cost = 0
    weight = 0
    for index, ratio in ratios:
        if treasures[index][0] + weight <= capacity:
            weight += treasures[index][0]
            best_cost += treasures[index][1]
            best_subset[index] = 1
    return best_cost, best_subset
