#Part 4: Combine Dynamic Programming with Monte Carlo and generate report

def final_subsets(treasures, opt_c):
    '''Use Monte Carlo simulation get opt_c and find the best subsets using opt_c'''
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
    
def write_opt(filename,N,n):
    '''write the combination into the cvs file'''
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


treasures=read_treasure('Knapsack_Instances.csv')
opt_c=mento_calor_opt(treasures[0:500], 50)
result01 = final_subsets(treasures[0:500],opt_c)
write_opt("Knapsack_solution_report.csv",500,50)