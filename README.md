# Knapsack-Problem
Several algorithms for solving 1/0 knapsack problem / combinatorial optimization in Python

1.	**Introduction**  
    1) **Problem Description**  
    Given a set of items, each with a weight and a value  
    Determine which items to be included in a collection so that the total weight is no more than a limited knapsack capacity and the total value is as large as possible  
    2) **Goals**  
    •	Given a certain knapsack capacity C, choose which items to put in the knapsack  
    •	Given a mix of the capacity Ci, choose the optimal capacity along with items put in the knapsack  

2.	**Approaches**  
There are three approaches in this problem:  
    •	Value/weight ratio  
    •	Dynamic programming  
    •	Monte Carlo simulation  
    1) **Value/weight ratio**: Calculate the value/weight ratio for each item and sort them from the highest ratio to the lowest ratio. Choose items according to the order unitl the total weight is more than limited capacity.  
    2) **Dynamic programming**: Consider all the possible weights from 1 to C as ci and all items weights as wj. If wj<ci, we have two possible actions: a) fill wj in the given ci and total value of ci will be vj+total value of (ci-wj), b) do not fill wj in the given ci and total value of ci = total value of ci-1. We take the maximum of these two possible action.   
    3) **Monte Carlo simulation**: This approach is to choose the optimal capacity among the mix of Ci. First, randomly assign a capacity for each knapsack following the given distribution. Second, get the best selection of each knapsack using value/weight ratio or dynamic programming approach and record the total value of each knapsack. Repeat the above simulation process for N times and select the capacity as optimal capacity giving the max total value.   
    
3.	**Files**  
    •	Test_example
        weight of item; value of item  
    •	Solution    
    •	Report 
        weight of item; value of item  
        sequence of 0/1: if the i-th element of sequence equal to 1 then we take the i-th item to knapsack overwise we don't take the item to knapsack
