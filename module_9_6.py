import itertools


def all_variants(text):
    _list = []
    for lst_1 in range(1, len(text) + 1):
        _list.append(list(itertools.combinations(text, lst_1)))
    for lst_2 in _list:
        for lst_3 in lst_2:
            if ''.join(lst_3) != 'ac':
                yield ''.join(lst_3)


a = all_variants("abc")
for i in a:
    print(i)
