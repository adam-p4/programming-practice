# Example: rgb(255, 255, 255) returns FFFFFF

def rgb(r, g, b):
    hexa = '0123456789ABCDEF'
    pairs = []
    # makes a list of lists e.g. [['F', 'F'], ['F', 'F'], ['F', 'F']]
    for el in (r, g, b):
        if el > 255:
            pairs.append(['F','F'])
        elif el < 0:
            pairs.append(['0','0'])
        else:
            pairs.append([hexa[el//16], hexa[el%16]])
    return ''.join(sum(pairs, []))
    
print(rgb(255, 2544, -255))