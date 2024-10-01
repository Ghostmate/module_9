from itertools import combinations


def all_variants(text):
    for i in range(len(text)):
        for k in combinations(text,i+1):
            result = ''
            for s in k:
                result += s
            yield result

a = all_variants("abc")
for i in a:
    print(i)