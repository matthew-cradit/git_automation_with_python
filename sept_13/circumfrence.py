import math

def foil(l): 
    d = 4.0
    c = d * math.pi
    while l >= c:
        l -= c
        d += (0.0025 * 2)
        c = d * math.pi
    
    return (round(d, 4) if l > c/2 or l == 0 else round(d + 0.0025, 4))
    
    


if __name__ == '__main__':
    print(foil(0))
    print(foil(50))
    print(foil(4321))
    print(foil(10000))
