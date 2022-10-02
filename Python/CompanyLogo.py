from itertools import groupby
if __name__ == '__main__':
    s = list(input())
    s.sort()
    dict_ = {}
    for (v, g) in groupby(s):
        dict_[v] = len(list(g))
    list_ = list(dict_.keys())
    list_.sort(reverse=True, key=lambda k: dict_[k])
    for char in list_[:3]:
        print(char, dict_[char])
        
