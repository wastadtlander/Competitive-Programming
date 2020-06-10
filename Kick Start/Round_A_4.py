for inc1 in range(int(input())):
    n, k = map(int, input().split())
    s = []
    sT = []
    for inc2 in range(int(n / k)):
        for inc3 in range(k):
            sT += input().split()
        s.append(sT)
        sT = []
    su = 0
    for inc2 in range(int(n / k)):
        for inc3 in range(k - 1):
            sT = s[inc2]
            sT.sort(key = len)
            for inc4 in range(len(sT[0])):
                if s[inc2][inc3][inc4] == s[inc2][inc3 + 1][inc4]:
                    su += 1
    print("Case #{}: {}".format(inc1 + 1, su))

# Test Case 1
# 2
# 2 2
# KICK
# START
# 8 2
# G
# G
# GO
# GO
# GOO
# GOO
# GOOO
# GOOO

# Test Case 2
# 1
# 6 3
# RAINBOW
# FIREBALL
# RANK
# RANDOM
# FIREWALL
# FIREFIGHTER

# Completed