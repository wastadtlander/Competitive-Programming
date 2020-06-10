for inc1 in range(int(input())):
    n = int(input())
    c = [int(inc2) for inc2 in input().split()]
    p = 0
    for inc2 in range(n - 2):
        if c[inc2] < c[inc2 + 1] and c[inc2 + 1] > c[inc2 + 2]:
            p += 1
    print("Case #{}: {}".format(inc1 + 1, p))

# Test Case

# 4
# 3
# 10 20 14
# 4
# 7 7 7 7
# 5
# 10 90 20 90 10
# 3
# 10 3 10

# Completed in 5:37.53 on 6/3/2020