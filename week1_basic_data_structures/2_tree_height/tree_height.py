# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def compute_height_fast(n, parents):
    tree = {}
    for c, p in enumerate(parents):
        if p not in tree:
            tree[p] = [c]
        else:
            tree[p].append(c)
            
    height = []        
    def traverse(i, count):
        if i not in tree:
            return
        height.append(count)    
        for p in tree[i]:
            traverse(p, count + 1)

    traverse(-1, 1)
    return max(height)                        



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_fast(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
