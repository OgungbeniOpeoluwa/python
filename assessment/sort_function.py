def my_sort_function(l1: list, numb=False):
    for n in range(len(l1)):
        for x in range(n + 1, len(l1)):
            if l1[n] > l1[x]:
                l1[n], l1[x] = l1[x], l1[n]
            if l1[n] < l1[x] and numb == True:
                l1[n], l1[x] = l1[x], l1[n]

    return l1


print(my_sort_function([15, 23, 3, 2, 45], True))
