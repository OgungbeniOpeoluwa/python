def is_pandlidrome(result: str) -> bool:
    results = []
    returns = ""
    for count in result:
        results.append(count)
    while len(results) != 0:
        returns += results.pop()
    if returns.lower() == result.lower():
        return True

