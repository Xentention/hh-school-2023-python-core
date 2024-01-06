from wine import Wine
from beer import Beer
from datetime import date

class Market:

    def __init__(self, wines: list = Wine, beers: list = Beer) -> None:
        self.drinks = dict((w.title, w) for w in wines) | dict((b.title, b) for b in beers)

    def has_drink_with_title(self, title=str) -> bool:
        return title in self.drinks

    def get_drinks_sorted_by_title(self) -> list:
        return list(dict(sorted(self.drinks.items())).values())

    def get_drinks_by_production_date(self, from_date=date, to_date=date) -> list:
        def check_date(pair) -> bool:
            key, value = pair
            return from_date <= value.production_date <= to_date;

        return list(dict(filter(check_date, self.drinks.items())).values())
