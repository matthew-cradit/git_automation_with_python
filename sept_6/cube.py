
def doesBrickFit(a, b, c, w,h): 
    return (w*h in [a*b, a*c, b*c])

if __name__ == '__main__':
    print(doesBrickFit(1,1,1,1,1))
    print(doesBrickFit(1,2,1,1,1))
    print(doesBrickFit(1,2,2,1,1))



    
