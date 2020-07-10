# Knapsack-problem with certain knapsack size C

'''Problem Description:
500 Knapsack Instances
C=100
Choose which items to put in the knapsack 
If you go over C, then you get nothing for that instance'''

# Part 2: Dynamic programming
'''Find the collection of items whoes total weight is no more than the limited knapsack size C
and the total value is the highest'''

def bag(weights,values,C,n):
    '''Find the total value we can get given a list of items
    
    Parameters
    ----------
    weights: list 
        the weights of all items
    values:  list
        the values of all items
    C: int
        the limited capacity
    n: int
        the number of items  
    Return
    ------
    matrix
        all possible item combinations with total weights satisfied capacity limitation
    '''
    bag=np.zeros((n+1,C+1),dtype=np.float32) 
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            bag[i][j] = bag[i - 1][j]
            if j >= weights[i - 1] and bag[i][j] < bag[i - 1][j - weights[i - 1]] + values[i - 1]:
                bag[i][j] = bag[i - 1][j - weights[i - 1]] + values[i - 1]
    return bag
    
 def best_subset(weights, bag, C, n):
    '''Find the combination of items with the highest value
    
    Parameters
    ----------
    weights: list 
        the weights of all items
    bag:  matrix 
        all possible item combinations with total weights satisfied capacity limitation
    C: int
        the limited capacity
    n: int
        the number of items  
    
    Return 
    ------
    list
        a list of 0/1 which is the best subset of items we select
    '''
    x = [0 for i in range(n)]
    j = C
    #print(bag[-1,-1])
    for i in range(n, 0, -1):
        if bag[i][j] > bag[i - 1][j]:
            x[i - 1] = 1
            j -= weights[i - 1]
    return(x)
