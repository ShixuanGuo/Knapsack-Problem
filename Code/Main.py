# 
treasures=read_treasure('Knapsack_Instances.csv')
opt_c=mento_calor_opt(treasures[0:500], 50)
result01 = final_subsets(treasures[0:500],opt_c)
write_opt("Knapsack_solution_report.csv",500,50)
