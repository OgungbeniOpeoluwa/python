def sum_list(result):
    returns = 0
    for numb in list(result):
        returns += sum(numb)
    return returns


def sum_list2(result):
    return filter(sum(list(result)), list(result))
