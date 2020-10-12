def sum_num(sum):
    """3+2+1"""
    if sum == 1:
        return 1
    else:
        return sum+sum_num(sum-1)


print(sum_num(3))