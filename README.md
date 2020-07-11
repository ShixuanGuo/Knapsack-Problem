# Knapsack-Problem
Several algorithms for solving 1/0 knapsack problem / combinatorial optimization in Python

## Part 1 Introduction  
1) **Problem Description**  
Given a set of items, each with a weight and a value  
Determine which items to be included in a collection so that the total weight is no more than a limited knapsack capacity and the total value is as large as possible  
2) **Goals**  
•	Given a certain knapsack capacity C, choose which items to put in the knapsack  
•	Given a mix of the capacity Ci, choose the optimal capacity along with items put in the knapsack  

## Part 2 Approaches  
1. Read the treasure information `treasures=read_treasure(file_name)` and saperate treasures' weights and values `weights,values=get_treasure(treasures)`  
2. There are three approaches to select treasures in this problem:  
•	Value/weight ratio  
•	Dynamic programming  
•	Monte Carlo simulation  
    1) **Value/weight ratio**: Calculate the value/weight ratio for each item and sort them from the highest ratio to the lowest ratio. Choose items according to the order unitl the total weight is more than limited capacity.  
    ```python
    best_cost, best_subset=value_weight_ratio(capacity,treasures)
    ```  
    2) **Dynamic programming**: Consider all the possible weights from 1 to C as ci and all items weights as wj. If wj<ci, we have two possible actions: a) fill wj in the given ci and total value of ci will be vj+total value of (ci-wj), b) do not fill wj in the given ci and total value of ci = total value of ci-1. We take the maximum of these two possible action.  
    ```python
    n=len(weights) # for multiple knapsacks, n is the total number of items would be selected in one knapsack
    best_value=bag(weights,values,capacity,n)
    subset=best_subset(weights,best_value,capacity,n)
    ```  
    3) **Monte Carlo simulation**: This approach is to choose the optimal capacity among the mix of Ci. First, randomly assign a capacity for each knapsack following the given distribution. Second, get the best selection of each knapsack using value/weight ratio or dynamic programming approach and record the total value of each knapsack. Repeat the above simulation process for N times and select the capacity as optimal capacity giving the max total value.  
    ```python
    opt_c=mento_calor_opt(treasures[0:500], 50)
    result = final_subsets(treasures[0:500],opt_c)
    ```  
3. Output our best subsets as a file using `write_opt("Knapsack_solution_report.csv",N,n)`.  
Have a quick look at a part of the first 3 knapsacks.  
![Part of solution](https://github.com/ShixuanGuo/Knapsack-Problem/blob/master/Part%20of%20solution.png)  
## Part 3 Files  
1) Test  
    * Test_example
        weight of item; value of item  
    * Report  
        weight of item; value of item  
    sequence of 0/1: if the i-th element of sequence equal to 1 then we take the i-th item to knapsack overwise we don't take the item to knapsack
2) Code(Solutions)      
    * Value_weight_raito  
    * Dynamic programming  
    * Monte Carlo simulation  
    * Generate_report  
    * Main (example using Dynamic programming and Monte Carlo)  
