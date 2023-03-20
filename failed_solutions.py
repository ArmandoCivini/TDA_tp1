import math
from matches import is_dominant

def search_single_match(posible_matches):
    for posible_match in posible_matches:
        if len(posible_match[1]) == 1:
            return posible_match
    return None

def search_match_least_peers(posible_matches):
    if not posible_matches:
        return [[], set()]
    min_matches = math.inf
    best_match = [[], set()]
    for posible_match in posible_matches:
        if len(posible_match[1]) == 0:
            continue
        if len(posible_match[1]) == 1:
            return posible_match
        if len(posible_match[1]) < min_matches:
            min_matches = len(posible_match[1])
            best_match = posible_match
    return best_match

def recursive_single_matches(point_match, point, posible_matches, matches, A):
    matches.append((point_match, point))
    A.remove(point_match)
    for posible_match in posible_matches:
        posible_match[1].discard(point_match)
    posible_match = search_single_match(posible_matches)
    if posible_match:
        matches, posible_matches, A = recursive_single_matches(posible_match[1].pop(), posible_match[0], posible_matches, matches, A)
    return matches, posible_matches, A

def iterative_minimum_matches(posible_matches, matches, A_matches):
    posible_match = search_match_least_peers(posible_matches)
    while len(posible_match[1]) >= 1:
        posible_matches.remove(posible_match)
        point_match = posible_match[1].pop()
        min_matches = A_matches[point_match]
        for selected_match in posible_match[1]:
            if A_matches[selected_match] < min_matches:
                point_match = selected_match
                min_matches = A_matches[selected_match]
        matches.append((point_match, posible_match[0]))
        for posible_match in posible_matches:
            posible_match[1].discard(point_match)
        
        posible_match = search_match_least_peers(posible_matches)
    return matches

def find_max_matching(A, B):
    #supuesto no hay puntos repetidos
    A = sorted(A, key=lambda point: point[0], reverse=True)
    B = sorted(B, key=lambda point: point[0], reverse=True)
    posible_matches = []
    matches = []
    A_matches = {}
    for point in A:
        A_matches[point] = 0

    for point in B: 
        point_matches = set()
        for point2 in A: #busco los matches posibles para point y los agrego a un set
            if is_dominant(point2, point):
                point_matches.add(point2)
                A_matches[point2] += 1
        if len(point_matches) == 1: #si hay un solo match, lo agrego a matches y saco ese punto de posible_matches y de A
            #ademas itero recursivamente para ir agregando todos los puntos que vayan quedando con un solo match
            matches, posible_matches, A = recursive_single_matches(point_matches.pop(), point, posible_matches, matches, A)
        elif len(point_matches) > 1:
            #si tiene mas de un match solo se agrega a la lista de posibles matches
            posible_matches.append((point, point_matches))
    matches = iterative_minimum_matches(posible_matches, matches, A_matches)
    # print(posible_matches)#remove for prod
    return matches

def find_max_matching2(A, B):
    A = sorted(A, key=lambda point: point[0], reverse=False)
    B = sorted(B, key=lambda point: point[0], reverse=True)
    posible_matches_B = {}
    posible_matches_A = {}
    matches = []
    for point in A:
        posible_matches_A[point] = set()
    for point in B:
        posible_matches_B[point] = set()

    for point_A in A: 
        for point_B in B:
            if is_dominant(point_A, point_B):
                posible_matches_A[point_A].add(point_B)
                posible_matches_B[point_B].add(point_A)
    
    go = True
    while go:
        point_match = None
        minimum_matches = math.inf
        is_in_A = True
        for point in posible_matches_A:
            if len(posible_matches_A[point]) < minimum_matches and len(posible_matches_A[point]) > 0:
                minimum_matches = len(posible_matches_A[point])
                point_match = point
        for point in posible_matches_B:
            if len(posible_matches_B[point]) < minimum_matches and len(posible_matches_B[point]) > 0:
                minimum_matches = len(posible_matches_B[point])
                point_match = point
                is_in_A = False
        if minimum_matches == math.inf:
            go = False
            continue
        if is_in_A:
            match_counter = posible_matches_A[point_match].pop()
            matches.append((point_match, match_counter))
            for point in posible_matches_B:
                posible_matches_B[point].discard(point_match)
            for point in posible_matches_A:
                posible_matches_A[point].discard(match_counter)
            posible_matches_A.pop(point_match)
            posible_matches_B.pop(match_counter)
        else:
            match_counter = posible_matches_B[point_match].pop()
            matches.append((point_match, match_counter))
            for point in posible_matches_A:
                posible_matches_A[point].discard(point_match)
            for point in posible_matches_B:
                posible_matches_B[point].discard(match_counter)
            posible_matches_B.pop(point_match)
            posible_matches_A.pop(match_counter)
    return matches