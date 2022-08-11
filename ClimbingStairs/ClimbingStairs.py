def solution(n):
    one, two = 1, 1
    for i in range(n - 1):
        two, one = one, one + two
    
    return one