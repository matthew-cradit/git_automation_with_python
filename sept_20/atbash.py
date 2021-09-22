switch = {
    'a':'z',
    'A':'Z',
    'b':'y',
    'B':'Y',
    'c':'x',
    'C':'X',
    'd':'w',
    'D':'W',
    'e':'v',
    'E':'V',
    'f':'u',
    'F':'U',
    'g':'t',
    'G':'T',
    'h':'s',
    'H':'S',
    'i':'r',
    'I':'R',
    'j':'q',
    'J':'Q',
    'k':'p',
    'K':'P',
    'l':'o',
    'L':'O',
    'm':'n',
    'M':'N'
}
def atbash(string):
    new_string = ''
    for x in string:
        if x in 'abcdefghijklm' or x in 'ABCDEFGHIJKLM':
            new_string += switch[x]
        elif x in 'nopqrstuvwxyz' or x in 'NOPQRSTUVWXYZ':
            new_string += list(switch.keys())[list(switch.values()).index(x)]
        else:
            new_string += x

    return new_string



if __name__ == '__main__':

    print(atbash('apple'))
    print(atbash('Hello world!'))
    print(atbash('Christmas is the 25th of December'))
