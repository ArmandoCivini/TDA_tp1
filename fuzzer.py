import random
from matches import find_max_matching, pretty_print_matches, is_dominant
from itertools import permutations
import sys


def remove_invalid_matches(matches):
    new_matches = []
    for match in matches:
        if is_dominant(match[0], match[1]):
            new_matches.append(match)
    return new_matches


def fuzzer_longer_A(set_length, iterations):
    for _ in range(iterations):
        A, B = [], []
        for _ in range(random.randint(set_length, set_length)):
            # random point in a graph
            a_point = (random.randint(-10, 10), random.randint(-10, 10))
            while a_point in A:
                a_point = (random.randint(-10, 10), random.randint(-10, 10))
            A.append(a_point)

        for _ in range(random.randint(1, set_length)):
            # random point in a graph
            b_point = (random.randint(-10, 10), random.randint(-10, 10))
            while b_point in B:
                b_point = (random.randint(-10, 10), random.randint(-10, 10))
            B.append(b_point)

        # consigo todos los matcheos posibles
        # https://www.geeksforgeeks.org/python-program-to-get-all-unique-combinations-of-two-lists/
        # no importa si son validos o no
        unique_combinations = []
        permut = permutations(A, len(B))
        for comb in permut:
            zipped = zip(comb, B)
            unique_combinations.append(list(zipped))

        maximum_match = []
        maximum_match_len = 0
        for matches in unique_combinations:
            cont = 0
            for match in matches:
                if is_dominant(match[0], match[1]):
                    cont += 1
            if cont > maximum_match_len:
                maximum_match_len = cont
                maximum_match = matches

        my_matches = find_max_matching(A, B)
        if maximum_match_len != len(my_matches):
            maximum_match = remove_invalid_matches(maximum_match)
            print("ERROR")
            print(f"A: {A}")
            print(f"B: {B}")
            print("")
            print("TRUE match:")
            pretty_print_matches(maximum_match)
            print("")
            print("my result:")
            pretty_print_matches(my_matches)
            return
    print("Every random test  generated passed")
    print("OK")
    return


def reverse_matches(matches):
    new_matches = []
    for match in matches:
        new_matches.append((match[1], match[0]))
    return new_matches


def fuzzer_longer_B(set_length, iterations):
    for _ in range(iterations):
        A, B = [], []
        for _ in range(random.randint(1, set_length)):
            # random point in a graph
            a_point = (random.randint(-10, 10), random.randint(-10, 10))
            while a_point in A:
                a_point = (random.randint(-10, 10), random.randint(-10, 10))
            A.append(a_point)

        for _ in range(random.randint(set_length, set_length)):
            # random point in a graph
            b_point = (random.randint(-10, 10), random.randint(-10, 10))
            while b_point in B:
                b_point = (random.randint(-10, 10), random.randint(-10, 10))
            B.append(b_point)

        # consigo todos los matcheos posibles
        # https://www.geeksforgeeks.org/python-program-to-get-all-unique-combinations-of-two-lists/
        # no importa si son validos o no
        unique_combinations = []
        permut = permutations(B, len(A))
        for comb in permut:
            zipped = zip(comb, A)
            unique_combinations.append(list(zipped))

        maximum_match = []
        maximum_match_len = 0
        for matches in unique_combinations:
            cont = 0
            rev_matches = reverse_matches(matches)
            for match in rev_matches:
                if is_dominant(match[0], match[1]):
                    cont += 1
            if cont > maximum_match_len:
                maximum_match_len = cont
                maximum_match = rev_matches

        my_matches = find_max_matching(A, B)
        if maximum_match_len != len(my_matches):
            maximum_match = remove_invalid_matches(maximum_match)
            print("ERROR")
            print(f"A: {A}")
            print(f"B: {B}")
            print("")
            print("TRUE match:")
            pretty_print_matches(maximum_match)
            print("")
            print("my result:")
            pretty_print_matches(my_matches)
            return
    print("Every random test  generated passed")
    print("OK")
    return


if __name__ == "__main__":
    fuzzer_longer_A(int(sys.argv[1]), int(sys.argv[2]))
