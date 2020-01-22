import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    sum1 = -1000
    r = len(arr[0])
    c = len(arr)
    for i in range(r-2):
        for j in range(c-2):
            sum2 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if(sum2 > sum1):
                sum1 = sum2
    return sum1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
