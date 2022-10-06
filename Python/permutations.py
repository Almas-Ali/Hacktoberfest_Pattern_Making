from itertools import permutations


def list_of_permutations(s, n):
    permutation_list = sorted(list(permutations(s, n)))
    for item in permutation_list:
        print("".join(item))


if __name__ == "__main__":
    string, number = input().split()
    list_of_permutations(string, int(number))
