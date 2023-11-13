def validate_subsequence(parent_list: list, sub_list):
    returns = True
    numb = []
    for count in sub_list:
        retrieve = parent_list.index(count)
        numb.append(retrieve)
    result = min(numb)
    results = max(numb)
    if numb.index(result) != 0 and numb.index(results) != len(numb)-1:
        returns = False
    return returns
