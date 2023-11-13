
def pizza_recommendation_app(result, hungry=0, super_hungry=0, classic=0):
    first_result = 0
    second_result = 0
    third_result = 0
    if hungry > 0 and super_hungry > 0 and classic > 0:
        first_result = get_size_of_stomach("hungry") * hungry
        second_result = get_size_of_stomach("super_hungry") * super_hungry
        third_result = get_size_of_stomach("classic") * classic
    total = get_total(first_result, second_result, third_result)
    results = get_number_of_boxes(result, total)
    remain = (results * get_pizza_slice(result)) - total
    price = get_pizza_price(result) * results
    return f'number of slice needed: {total} number of boxes: {results} number of slice left: {remain} total: {price}'


def get_pizza_price(key: str):
    pizza_price = {"big": 5000, "medium": 4000, "small": 1200}
    return pizza_price.get(key.lower())


def get_pizza_slice(key: str):
    available_pizza_size = {"big": 10, "medium": 6, "small": 4}
    return available_pizza_size.get(key.lower())


def get_size_of_stomach(key: str):
    stomach_size = {"hungry": 2, "super_hungry": 4, "classic": 1}
    return stomach_size.get(key.lower())


def get_total(hungry=0, super_hungry=0, classic=0):
    total = hungry + super_hungry + classic
    return total


def get_number_of_boxes(key, total):
    result = get_pizza_slice(key)
    returns = 0
    if total % result != 0:
        returns = total // result
        returns += 1
    else:
        returns = total // result
    return returns
