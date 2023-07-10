from os import *
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    largest = arr[0]
    for i in range(0,n):
        if arr[i]>largest:
            largest = arr[i]
    return largest

