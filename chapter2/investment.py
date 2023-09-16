principal = 1000
profit = 7
number_of_year1 = 10
number_of_year2 = 20
number_of_year3 = 30

percentage = 7 / 100

first_value = (1 + percentage) ** number_of_year1

ten_years = principal * first_value

second_value = (1 + percentage) ** number_of_year2

twenty_years = principal * second_value

third_value = (1 + percentage) ** number_of_year3

thirty_years = principal * third_value

print("Money expected after 10 years : ", ten_years)

print("Money expected after 20 years : ", twenty_years)

print("Money expected after 30 years : ", thirty_years)
