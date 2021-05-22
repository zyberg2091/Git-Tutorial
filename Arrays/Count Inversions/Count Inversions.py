#User function Template for python3
"""TLE ERROR"""
"""It needs optmized algo"""

# arr[]: Input Array
# N : Size of the Array arr[]
#Function to count inversions in the array.
def inversionCount(self, a,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                count+=1
    
    return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends