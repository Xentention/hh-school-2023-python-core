from wine import Wine
from beer import Beer
from market import Market
from datetime import date

wines = [
    Wine("wine1", date.fromisoformat('2019-12-04')), 
    Wine("wine2", date.fromisoformat('2020-12-04')), 
    Wine("wine3", date.fromisoformat('2021-12-04'))
]

beers = [
    Beer("beer1", date.fromisoformat('2019-12-04')), 
    Beer("beer2", date.fromisoformat('2020-12-04')), 
    Beer("beer3", date.fromisoformat('2021-12-04'))
]

market = Market(wines, beers)

print('Has drink:')
print(f'Should be true: {market.has_drink_with_title("wine1")}')
print(f'Should be false: {market.has_drink_with_title("wine5")}')

print('\n<------------>\n')

print('Sorted by title:')
print(market.get_drinks_sorted_by_title())

print('\n<------------>\n')

print('Get by prod date:')
print(f"All: {market.get_drinks_by_production_date(date.fromisoformat('2019-12-04'),  date.fromisoformat('2023-12-04'))}")
print(f"1 Wine 1 Beer: {market.get_drinks_by_production_date(date.fromisoformat('2019-12-04'),  date.fromisoformat('2019-12-05'))}")
print(f"None: {market.get_drinks_by_production_date(date.fromisoformat('2023-12-04'),  date.fromisoformat('2023-12-04'))}")
