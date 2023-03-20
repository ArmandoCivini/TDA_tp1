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
    available_points = [] #heap, ordena en de menor a mayor valores de y

    curr_B_index = 0
    for i in range(len(A)-1):
        
        x_start = A[i][0]
        x_end = A[i+1][0]
        heappush(available_points, (A[i][1], A[i])) #guardo el punto actual como disponible

        possible_B, curr_B_index = get_all_possible_B(B, x_start, x_end, curr_B_index)

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