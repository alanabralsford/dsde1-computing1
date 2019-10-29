import math

def period(L, g):
    if (not isinstance(L, (int, float))) or (not isinstance(g, (int, float))):
        print('TypeError')
        raise TypeError
    if (L <= 0 or g == 0):
        print('ValueError')
        raise ValueError
    within = L / g
    ans = (math.sqrt(within)) * 2 * math.pi
    print(ans)
    return ans

#period(3.3, 9.81)
