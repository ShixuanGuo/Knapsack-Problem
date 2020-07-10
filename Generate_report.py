#Part 1: Get the information

#Read the file
def read_treasure(file_name):
    '''The input file has format like: nth row:weights, (n+1)th row:values, n=0,...max_row
    
    file_name: str
        name of input file
    '''
    f=open(file_name, 'r')
    lines=f.readlines()
    treasures=[[lines[i].strip('\n'),lines[i+1].strip('\n')] \
              for i in range(0,1500,3)]
    return treasures

#Get the weights and values of all items
def get_treasure(treasure):
    '''Separate items' weights and values
    
    Parameters
    ---------
    treasure: list
    
    Return
    ------
    weights: list
        list of items' weights
    values: list
        list of items' values
    '''
    weights=treasure[0].split(',')
    values=treasure[1].split(',')
    for i in range(len(weights)):
        weights[i]=int(weights[i]) 
        values[i]=float(values[i]) 
    return weights, values


#Part 4: Generate report
    
def write_opt(filename,N,n):
    '''write the combination into the cvs file
    
    Parameters
    ----------
    file_name: str
        name of input file
    N: int
        the number of simulations
    n: int
        the number of items waiting to be selected in one knapsack
    '''
    first_line = open('Knapsack_Instances.csv','r') .readlines()[::3]
    first_list = []
    for a in first_line:
        p1 = a.strip("\n").split(",")
        first_list.append(p1)
    line1 = first_list
    second_line = open('Knapsack_Instances.csv','r').readlines()[1::3]
    second_list = []
    for b in second_line:
        p2 = b.strip("\n").split(",")
        second_list.append(p2)
    line2 = second_list
    wr = open(filename,"w")   
    for i in range(N):
        for j in range(n-1):
            wr.write(str(line1[i][j]))
            wr.write(',') 
        wr.write(str(line1[i][n-1]))
        wr.write('\n')
        for j in range(n-1):
            wr.write(str(line2[i][j]))
            wr.write(',')
        wr.write(str(line2[i][n-1]))
        wr.write('\n')
        for j in range(n-1):
            wr.write(str(result01[i][j]))
            wr.write(',')
        wr.write(str(result01[i][n-1]))
        wr.write('\n')    
    wr.close()
    return filename

# Example
treasures=read_treasure('Knapsack_Instances.csv')
opt_c=mento_calor_opt(treasures[0:500], 50)
result01 = final_subsets(treasures[0:500],opt_c)
write_opt("Knapsack_solution_report.csv",500,50)
