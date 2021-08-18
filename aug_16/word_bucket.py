
def bucketize( var, n):
    words = var.split(' ')
    result = []
    phrase = ''
    for word in words:
        if len(phrase) + len(word) > n:
            result.append(phrase.rstrip())
            phrase = word + ' '

        else:
            phrase += str(word) + ' '
    result.append(phrase.rstrip())
    return result
    

if __name__ == '__main__':
    print( bucketize("she sells sea shells by the sea", 10))
    print( bucketize("the mouse jumped over the cheese", 7))
    print( bucketize("fairy dust coated the air", 20))
    print( bucketize("a b c d e", 2))
