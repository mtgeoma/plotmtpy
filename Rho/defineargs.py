from itertools import cycle

def args(argts):
    
    components = []
    files = []
    z = []
    
    for a in argts:
        if a in ('ZXX', 'ZYY', 'ZXY', 'ZYX'):
            components.append(a)
        elif a in ('rhoa', 'phi'):
            z.append(a)
        else:
            files.append(a)
    
    return components, files, z

            
def lines(components):
    
    if len(components) == 1:
        colors = cycle(['blue', 'red', 'green', 'yellow'])
        fmts = cycle(['o'])
    
    elif len(components) == 2:
        colors = cycle(['blue','blue', 'red', 'red', 'green', 'green', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o'])
        
    elif len(components) == 3:
        colors = cycle(['blue','blue', 'blue', 'red', 'red', 'red', 
                        'green', 'green', 'green', 'yellow', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o', '^'])

    else:
        colors = cycle(['blue','blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 
                        'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o', '^', 'd'])
        
    return colors, fmts
        
if (__name__=="__main__"):
    pass