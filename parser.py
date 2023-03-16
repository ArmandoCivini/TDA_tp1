

def parser(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        A = []
        B = []
        for line in lines:
            a_and_b = line.split()
            A.append(tuple([int(x) for x in a_and_b[0].split(',')]))
            B.append(tuple([int(x) for x in a_and_b[1].split(',')]))
        return A, B