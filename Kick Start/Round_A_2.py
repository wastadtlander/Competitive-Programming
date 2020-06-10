for I in range(int(input())):
    N, K, P = [int(II) for II in input().split()]
    S = []
    for III in range(N):
        S.append([int(IV) for IV in input().split()])
    B = 0
    sT = []
    for V in range(P):
        for VI in range(len(S)):
            if not S[VI]:
                S.pop(VI)
            sT.append(S[VI][0])
            if len(sT) == len(S):
                B += max(sT)
                S[sT.index(max(sT))].remove(max(sT))
                break
        sT = []
    print("Case #{}: {}".format(I + 1, B))


# Test Cases
# 2
# 2 4 5
# 10 10 100 30
# 80 50 10 50
# 3 2 3
# 80 80
# 15 50
# 20 10
# Completed