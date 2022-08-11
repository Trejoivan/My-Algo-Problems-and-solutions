def solution(n):
    one, two = 1, 1
    for i in range(n - 1):
        two, one = one, one + two
    
    return one

# with the bottom up solution , you are solving sub problems by incremening one's value as you go from the end to the begining of the array
