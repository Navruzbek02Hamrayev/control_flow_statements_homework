def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a<0 and b<0 and c<0:
        return 3
    if a>0 and b<0 and c<0:
        return 2
    if a<0 and b>0 and c<0:
        return 2
    if a<0 and b<0 and c>0:
        return 2
    if a<0 and b>0 and c>0:
        return 1
    if a>0 and b<0 and c>0:
        return 1
    if a>0 and b>0 and c<0:
        return 1
print(main(-2,4,1))
print(main(3,-3,-6))