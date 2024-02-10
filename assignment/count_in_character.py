def returnCharacterAndCount(inputs):
    dicts = {}
    for counts in inputs:
        if dicts.keys() == counts:
            continue
        dicts[counts] = inputs.count(counts)
    return dicts


