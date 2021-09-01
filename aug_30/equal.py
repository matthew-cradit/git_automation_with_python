class Equallity:
    

    def __eq__(self, value):
        test = type(value)
        
        return test == type(value)


if __name__ == '__main__':

    equal = Equallity()

    print(equal == [])
    print(equal == ())
    print(equal == (lambda:1))
