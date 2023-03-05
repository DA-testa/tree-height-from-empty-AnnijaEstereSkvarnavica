# python3

import sys
import threading


def compute_height(n, parents):
    # Create a list of lists to store the children of each node
    children = [[] for _ in range(n)]
    
    # For each node, append it to the list of children of its parent
    for child, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(child)
    
    # Define a recursive function to get the height of a node
    def get_height(node):
        if not children[node]:
            # If the node has no children, its height is 1
            return 1
        else:
            # If the node has children, its height is 1 plus the maximum height of its children
            return 1 + max(get_height(child) for child in children[node])
    
    # Find the root node (the node with no parent) by finding the index of -1 in the parents list
    root = parents.index(-1)
    
    # Return the height of the tree rooted at the root node
    return get_height(root)
    
    # Your code here
    #return max_height


def main():
    input_type = int(input())
    if input_type == 'I':  
        n = int(input()) 
    
        
        
    elif input_type == 'F':
        fileName = int(input()) 
        if 'a' in fileName:
            print("error")
            return
        try:
            with open('test/' + fileName, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("error")
            return
        
        except ValueError:
            print("error")
            return
        
            
    else:
        print("error")                                                                     
        
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



