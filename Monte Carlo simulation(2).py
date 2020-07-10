#Knapsack problem with uncertain knapsack size (multiple Cs followed a distribution)

'''Problem Description:
500 Knapsack Instances 
C in U[100,150] 
Find out C once you choose which items to put in the knapsack 
If you go over C, then you get nothing for that instance 
'''

#Part 3: Monte Carlo simulation
#continue with dynamic programming

def mento_calor_opt(treasures, N):
    '''trail: f(C)
    for each set, randomly assign a C follow the uniform distribution: U(100,150), 
    record total value of all sets and repeat the simulation for N times
    find the optimal C for each set giving the max total value among N total value
    
    Parameters
    ---------
    treasures: list
        combination list of treasures' weights and values
    N: int
        the number of simulations
    
    Return
    ------
    opt_c: float
        the best capcaity assigned to knapsacks
    '''
    opt_c=100
    max_value=0
    for C2 in range(100,151):
        total_value=0
        expect_best_value=0
        for C in list(np.random.uniform(100,150,N)):
            current_weight=0
            for treasure in treasures:
                weights,values=get_treasure(treasure)
                n=len(weights)
                best_value=bag(weights,values,C2,n)
                subset=best_subset(weights,best_value,C2,n)
                for i in range(n):
                    current_weight+=subset[i]*weights[i]
                if current_weight<=C:
                    total_value+=best_value[-1,-1]
        expect_best_value=total_value/N
        if expect_best_value>max_value:
            max_value=expect_best_value
            opt_c=C2
    return opt_c

# Combine Dynamic Programming with Monte Carlo 
def final_subsets(treasures, opt_c):
    '''Use Monte Carlo simulation get opt_c and find the best subsets using opt_c
    
    Parameters
    ---------
    treasures: list
        combination list of treasures' weights and values
    opt_c: float
        the best capcaity assigned to knapsacks
    
    Return
    ------
    total_subset: list
        a list of best subsets for all knapsacks
    '''
    result=[]
    total_subset = []
    for treasure in treasures:
        weights,values=get_treasure(treasure)
        n=len(weights)
        best_value=bag(weights,values,opt_c,n)
        subset=best_subset(weights,best_value,opt_c,n)
        result+=[best_value, subset]
        total_subset += [subset]
    
    return total_subset
