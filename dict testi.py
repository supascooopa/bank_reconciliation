# a = ["a", "a", "a", "b", "c"]
# b = [1, 2, 3, 4, 5]
# c = {}
# print(c)

a = {"a": [["hello"], ["again"]], "b": [["friendly"],["spidey"]], "c": [["Venom"],["&"]]}
b = {"a": [["friend"]], "b": [["neigborhood"]], "d": [["Carnage"]]}

matching = [a[i][0] and b[i][0] for i, j in zip(a.keys(), b.keys()) if i == j]
print(matching)