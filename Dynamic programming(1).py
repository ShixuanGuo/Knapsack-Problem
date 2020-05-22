# Knapsack-problem with certain knapsack size C

'''Problem Description:
500 Knapsack Instances
C=100
Choose which items to put in the knapsack 
If you go over C, then you get nothing for that instance'''

#Part 1: Get the information

#Read the file
def read_treasure(file_name):
    '0:weight; 1:value'
    f=open(file_name, 'r')
    lines=f.readlines()
    treasures=[[lines[i].strip('\n'),lines[i+1].strip('\n')] \
              for i in range(0,1500,3)]
    return treasures

#Get the weights and values of all items
def get_treasure(treasure):
    weights=treasure[0].split(',')
    values=treasure[1].split(',')
    for i in range(len(weights)):
        weights[i]=int(weights[i]) 
        values[i]=float(values[i]) 
    return weights, values


# Part 2: Dynamic programming
'''Find the collection of items whoes total weight is no more than the limited knapsack size C
and the total value is the highest'''

def bag(weights,values,C,n):
    '''Find the total value we can get, 
    given the weights and values of all items, the number of items and the limited size (C) 
    '''
    bag=np.zeros((n+1,C+1),dtype=np.float32) 
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            bag[i][j] = bag[i - 1][j]
            if j >= weights[i - 1] and bag[i][j] < bag[i - 1][j - weights[i - 1]] + values[i - 1]:
                bag[i][j] = bag[i - 1][j - weights[i - 1]] + values[i - 1]
    return bag
    
 def best_subset(weights, bag, C, n):
    '''Find the combination of items with the highest value,
    return a list of 0/1 
    '''
    x = [0 for i in range(n)]
    j = C
    #print(bag[-1,-1])
    for i in range(n, 0, -1):
        if bag[i][j] > bag[i - 1][j]:
            x[i - 1] = 1
            j -= weights[i - 1]
    return(x)