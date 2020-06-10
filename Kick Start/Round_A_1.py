for _ in range(int(input())):
    N, B = map(int, input().split())
    A = sorted(map(int, input().split()))
    t = 0
    for _i in range(len(A)):
        if t + A[_i] > B:
            print("Case #{}: {}".format(_ + 1, _i))
            break
        else:
            t += A[_i]

# Test Case
# 3
# 4 100
# 20 90 40 90
# 4 50
# 30 30 10 10
# 3 300
# 999 999 999

# Completed