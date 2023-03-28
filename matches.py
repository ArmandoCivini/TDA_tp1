from parser import parser, parser_internal
import sys
import math
from heapq import heappush, heappop, heapify
import bisect
from sortedcontainers import SortedList

def pretty_print_matches(matches):
    print(f"Tamaño del matching: {len(matches)}")
    print("Matching:")
    print("(A → B)")
    for match in matches:
        print(f"{match[0]} → {match[1]}")

def is_dominant(a, b):
    return a[0] >= b[0] and a[1] >= b[1]

def sort_points_by_x(points):
    return sorted(points, key=lambda point: point[0], reverse=True)

def sort_sets(A, B):
    A = sort_points_by_x(A)
    B = sort_points_by_x(B)
    A.append((-math.inf, -math.inf)) #truco para que en la ultima iteracion use todos los puntos de B
    return A, B

def get_all_possible_B(B, x_start, x_end, curr_B_index):
    possible_B = [] #heap, acumulo todos los puntos de B que estan en el rango de x del A actual y el siguiente
    #se ordenan en y de menor a mayor y se descartan al final de la iteracion

    for point_B in B[curr_B_index:]: #busco todos los puntos de B entre x_start y x_end
        if point_B[0] > x_start:
            curr_B_index += 1
            continue
        if point_B[0] <= x_end:
            break
        heappush(possible_B, (point_B[1], point_B))
        curr_B_index += 1
    return possible_B, curr_B_index

def find_max_matching(A, B):
    A, B = sort_sets(A, B) #ordeno por x de mayor a menor

    matches = []
    available_points = SortedList(key=lambda point: point[1]) #heap, ordena en de menor a mayor valores de y

    curr_B_index = 0
    for i in range(len(A)-1):
        
        x_start = A[i][0]
        x_end = A[i+1][0]
        available_points.add(A[i]) #guardo el punto actual como disponible

        possible_B, curr_B_index = get_all_possible_B(B, x_start, x_end, curr_B_index)

        for _ in range(len(possible_B)):
            B_point = heappop(possible_B)
            A_match_indx = available_points.bisect_left(B_point[1])
            if A_match_indx == len(available_points):
                continue
            A_match = available_points[A_match_indx]
            matches.append((A_match, B_point[1]))
            available_points.remove(A_match)
        
    return matches

def algorithm_with_paths(n, filenameA, filenameB):
    A, B = parser(filenameA, filenameB)
    matches = find_max_matching(A, B)
    pretty_print_matches(matches)

def main():
    argc = len(sys.argv)
    if argc == 2: 
        path = sys.argv[1]
        A, B = parser_internal(path)
        matches = find_max_matching(A, B)
        pretty_print_matches(matches)
    elif argc == 4:
        n = int(sys.argv[1])
        filenameA = sys.argv[2]
        filenameB = sys.argv[3]
        algorithm_with_paths(n, filenameA, filenameB)
    else:
        print("invalid amount of arguments")

if __name__ == "__main__":
    main()