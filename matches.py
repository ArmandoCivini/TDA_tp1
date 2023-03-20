from parser import parser
import sys
import math
from heapq import heappush, heappop, heapify

def pretty_print_matches(matches):
    print(f"Tamaño del matching: {len(matches)}")
    print("Matching:")
    print("(A → B)")
    for match in matches:
        print(f"{match[0]} → {match[1]}")

def is_dominant(a, b):
    return a[0] >= b[0] and a[1] >= b[1]

def find_max_matching(A, B):
    A = sorted(A, key=lambda point: point[0], reverse=True)
    B = sorted(B, key=lambda point: point[0], reverse=True)
    A.append((-1, -1)) #truco para que en la ultima iteracion use todos los puntos de B

    matches = []
    available_points = [] #heap, ordena en de menor a mayor valores de y

    curr_B_index = 0
    for i in range(len(A)-1):
        possible_B = []
        x_start = A[i][0]
        x_end = A[i+1][0]
        heappush(available_points, (A[i][1], A[i]))
        for point_B in B[curr_B_index:]:
            if point_B[0] > x_start:
                curr_B_index += 1
                continue
            if point_B[0] <= x_end:
                break
            heappush(possible_B, (point_B[1], point_B))
            curr_B_index += 1
        used_A = []
        tuple_B = None
        while len(available_points) > 0 and (len(possible_B) > 0 or tuple_B is not None):
            tuple_A = heappop(available_points)
            if tuple_B is None: #solo saco otro b si en la iteracion anterior se matcheo
                tuple_B = heappop(possible_B)
            if tuple_A[0] >= tuple_B[0]:
                matches.append((tuple_A[1], tuple_B[1]))
                tuple_B = None
            else:
                used_A.append(tuple_A)
        used_A.extend(available_points) #recupero los puntos de A que no se usaron
        available_points = used_A
    return matches

def main():
    path = sys.argv[1]
    A, B = parser(path)
    matches = find_max_matching(A, B)
    pretty_print_matches(matches)

if __name__ == "__main__":
    main()