# Complete the lonelyinteger function 
# lonelyinteger has the following parameter(s):
#  int a[n]: an array of integers
# Returns int: the element that occurs only once


def lonelyinteger(a):
    return list(set(a))[a.index(list(set(a))[0])]

