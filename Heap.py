import math

#Max heapify an element of input array
def MaxHeapify(A, i):
    l = (i+1)*2 - 1
    r = (i+1)*2 
    
    if l < len(A) and A[l] > A[i]:
        largest = l
    else: 
        largest = i
    
    if r < len(A) and A[r] > A[largest]:
        largest = r
        
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        MaxHeapify(A, largest)
        

#builds a max heap from a given array by calling heap
def BuildMaxHeap(A):
    for i in reversed(range(0, len(A)//2)):
        MaxHeapify(A, i)
    return A
   
#get first element of heap because by definition that's the biggest one     
def HeapMaximum(A):
    return A[0]

#extract first element of heap and rebuild heap
def ExtractHeapMaximum(A):
    heapMax = A[0]
    A[0] = A.pop()
    MaxHeapify(A, 0)
    return heapMax 

#insert element into end of max heap and call heapify on it
def MaxHeapInsert(A,x):
    A.append(x)
    i = len(A) - 1
    while A[i] > A[i//2] and i > 0:
        A[i],A[i//2] = A[i//2],A[i]
        i -= 1
        
    return A


def HeapSort(A):
    BuildMaxHeap(A)
    sortedHeap = []
    for i in range(len(A)-1,-1,-1):
        A[i],A[0] = A[0],A[i]
        sortedHeap.insert(0,A[-1])
        del A[-1]
        MaxHeapify(A,0)
    return sortedHeap

#prints heap as an array
def PrintAsArray(A):
    print(A) 


#make a matrix of a size dependent on the size of the input array
def makeMatrix(A):
    maxDepth = int(math.log2(len(A))) + 1
    height = 0
    for i in range(maxDepth):
        height += 2**i
    matrix = [[" " for i in range(height)] for j in range(maxDepth)]
    return matrix

#fill the matrix with the contents of the input array such that it resembles a binary tree
def fillMatrix(A, i, matrix, begin, end, depth):
    if depth >= len(matrix) or i >= len(A):
        return matrix
    mid = (end+begin)//2
    matrix[depth][mid] = A[i]
    
    fillMatrix(A,(i+1)*2 -1,matrix,begin,mid-1,depth+1)
    fillMatrix(A,(i+1)*2 ,matrix,mid+1,end,depth+1)
    
    return matrix
    
#transpose matrix into a sideways binary tree and print it (I'm aware I could've made it sideways initially but due time is approaching and I'm tired)
def PrintAsTree(A):
    maxDepth = int(math.log2(len(A))) + 1
    height = 0
    for i in range(maxDepth):
        height += 2**i
    tree = [[" " for i in range(maxDepth)] for j in range(height)]
    matrix = fillMatrix(A, 0, makeMatrix(A),0,14,0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tree[j][i] = matrix[i][j]
    
    
    for i in range(len(tree)):
        print(*tree[i])
    
    
    
def main():
    arr = [2,4,1,9,3,7,8,10,14,16]
    
    BuildMaxHeap(arr)
    
    PrintAsArray(arr)
    
    PrintAsTree(arr)
    
    print(HeapMaximum(arr))
    
    arr2=arr    
    print(ExtractHeapMaximum(arr2))
    print(arr2)
    
    arr3 = arr
    print(HeapSort(arr3))
    
    
    
    
    
    

if __name__ == "__main__":
    main()
    
