# python3

import sys
import threading


def compute_height(n, parents):
    telements = [[] for i in range(n)]
    roots = set(range(n))
    for j in range(n):
        if parents[j] != -1:
            telements[parents[j]].append(j)
            roots.discard(j)
    
    if len(roots) != 1:
        raise ValueError("Input does not represent a valid tree.")
    
    root = roots.pop()
    
    def height(node):
        return max([height(child) for child in telements[node]] or [0]) + 1
    
    return height(root)
   


def main():
    input_type = input()
    if input_type == 'I':  
        n = int(input()) 
        parents = list(map(int, input().split()))
    elif input_type == 'F':
        fileName = input().strip()
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
        print("error: invalid input type")
        return
    

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



