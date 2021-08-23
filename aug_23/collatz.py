#collatzs calculations 
def collatz(x):
    result = 0
    while x > 1:
        x = x // 2 if x % 2 == 0 else 3*x+1 
        result += 1

    return result
#returns shortest seq
def test(a, b):
    if a <= 1 or b <= 1:
        return "[error] must be positive integers"
    else:
        return "a" if collatz(a) < collatz(b) else "b"


if __name__ == "__main__":
    print(test(10,15))
    print(test(13,16))
    print(test(53782,72534))
    print(test(-2,0))
    print(test(45, -3))
