# def biggest_odd(number: str):
#     counts = []
#     for count in number:
#         if int(count) % 2 == 1:
#             counts.append(count)
#     maxi = counts[0]
#     for numbers in counts:
#         if numbers > maxi:
#             maxi = numbers
#     return maxi


def biggest_odds(numbers):
    return list(filter(lambda number: int(number) % 2 == 1, numbers))


print(biggest_odds("23445789"))
