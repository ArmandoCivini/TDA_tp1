

def parser_internal(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        A = []
        B = []
        for line in lines:
            a_and_b = line.split()
            A.append(tuple([int(x) for x in a_and_b[0].split(',')]))
            B.append(tuple([int(x) for x in a_and_b[1].split(',')]))
        return A, B
    
def parser(filenameA, filenameB):
    A = []
    B = []
    with open(filenameA, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x, y = line.split()
            x = float(x.replace(',', '.'))
            y = float(y.replace(',', '.'))
            A.append((x, y))

    with open(filenameB, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x, y = line.split()
            x = float(x.replace(',', '.'))
            y = float(y.replace(',', '.'))
            B.append((x, y))

    return A, B