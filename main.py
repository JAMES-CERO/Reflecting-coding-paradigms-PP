# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def sortNflatt(arr):
    result = sorted(sum(arr, []))
    print("The sorted and flattened list : " + str(result))

sortNflatt([[1,3],[2,3,4], [0,3,4]])