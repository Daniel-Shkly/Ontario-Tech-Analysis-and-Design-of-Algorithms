import numpy as np


# PART A

def GreedyCut(log):
    
    return ActualGreedyCut(1,len(log)-2,log)

def ActualGreedyCut(start, end, log):
    
    # base case
    if start > end:
        return 0
    
    # get the point closest to the middle
    mid = log[-1]/2
    
    minFromMiddle = float('inf')
    indexMin = float('inf')
    
    for i in range(start,end+1):
        if abs(log[i] - mid) < minFromMiddle:
            minFromMiddle = abs(log[i] - mid)
            indexMin = i
    
    
    # calculate the cost: (cost of cutting initial) + (cost left log) + (cost right log)
    cost = log[end+1] - log[start-1] + ActualGreedyCut(start,indexMin-1, log) + ActualGreedyCut(indexMin+1, end, log)
    
    return cost



# PART B 

def DynamicCut(log):
    
    # create a matrix to store sub problem values in
    dp = np.zeros((log[-1],log[-1]))
    for i in range(log[-1]):
        for j in range(log[-1]):
            dp[i][j] = -1
    
    return ActualDynamicCut(1, len(log)-2, log, dp)


def ActualDynamicCut(start, end, log, dp): 
    
    # base case
    if start > end:
        return 0
    
    # if sub problem solution already exists, grab it from the matrix
    if dp[start][end] != -1:
        return dp[start][end]
    
    minCost = float('inf')
    
    # iterate through the log
    for i in range(start,end+1):
        
        # get cost of each sequence of cuts: (initial cost) + (cost left) + (cost right)
        testCut = log[end+1] - log[start-1] + ActualDynamicCut(start, i-1, log, dp) + ActualDynamicCut(i+1, end, log, dp)
        
        # keep the smallest cost
        minCost = min(minCost,testCut)
    
    # store solution in matrix
    dp[start][end] = minCost
    
    return minCost 
    
 

def main():
    
    print(GreedyCut([0,7,8,9,16]))
    
    print(DynamicCut([0,7,8,9,16]))
    


if __name__ == "__main__":
    main()
