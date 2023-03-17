from parser import parser
import sys

def is_dominant(a, b):
    return a[0] >= b[0] and a[1] >= b[1]

def search_single_match(posible_matches):
    for posible_match in posible_matches:
        if len(posible_match[1]) == 1:
            return posible_match
    return None

def recursive_single_matches(point_match, point, posible_matches, matches, A):
    matches.append((point_match, point))
    A.remove(point_match)
    for posible_match in posible_matches:
        posible_match[1].discard(point_match)
    posible_match = search_single_match(posible_matches)
    if posible_match:
        matches, posible_matches, A = recursive_single_matches(posible_match[1].pop(), posible_match[0], posible_matches, matches, A)
    return matches, posible_matches, A

path = sys.argv[1]
A, B = parser(path)
#supuesto no hay puntos repetidos
posible_matches = []
matches = []
for point in B: 
    point_matches = set()
    for point2 in A: #busco los matches posibles para point y los agrego a un set
        if is_dominant(point2, point):
            point_matches.add(point2)
    if len(point_matches) == 1: #si hay un solo match, lo agrego a matches y saco ese punto de posible_matches y de A
        #ademas itero recursivamente para ir agregando todos los puntos que vayan quedando con un solo match
        matches, posible_matches, A = recursive_single_matches(point_matches.pop(), point, posible_matches, matches, A)
    elif len(point_matches) > 1:
        #si tiene mas de un match solo se agrega a la lista de posibles matches
        posible_matches.append((point, point_matches))

print(posible_matches)
print(matches)