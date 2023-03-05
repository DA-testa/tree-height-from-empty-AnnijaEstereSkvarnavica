# python3

import sys
import threading


def compute_height(n, parents):
    telements = [[] for i in range(x)]                 
    for j in range (x):
        if parents[j] == -1: 
            root = 1 
        else:
            telements[parents[j]].append(j)
    def dfs(node, depth):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for child in adj_list[node]:
            dfs(child, depth+1)
    
    max_depth = 0
    dfs(root, 1)
    return max_depth

    
    # Your code here
    #return max_height


def main():
    input = input()
    if input == 'I':  
        x = int(input()): 
    elif input == 'F':
        fileName = input()
        if 'a' in filename:
            print("error")
            return
        try:
            with open('folder/' + filename, 'r') as f:
                x = int(f.readline())
                parents = list(map(int,input().split())) 
        except FileNotFoundError:
            print("error")
            return
    else:
        ("error")                                                                     
        
    print(compute_height(n,parents))

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()



