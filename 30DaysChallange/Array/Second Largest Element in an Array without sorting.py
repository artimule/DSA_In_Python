
def second_largest(a, n):
    largest = a[0]
    slargest = -1
    for i in range(1, n):
        if a[i] > largest:
            slargest = largest
            largest = a[i]
        elif a[i] < largest and a[i] > slargest:
            slargest = a[i]
    return slargest

def second_smallest(a, n):
    smallest = a[0]
    ssmallest = float('inf')
    for i in range(1, n):
        if a[i] < smallest:
            ssmallest = smallest
            smallest = a[i]
        elif a[i] != smallest and a[i] < ssmallest:
            ssmallest = a[i]
    return ssmallest

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    slargest = second_largest(a, n)
    ssmallest = second_smallest(a, n)
    return [slargest, ssmallest]
