class Market:

    def __init__(self, wines: list = None, beers: list = None) -> None:
        drinks_list = wines + beers
        self.drinks = dict((d.title, d) for d in drinks_list)

    def has_drink_with_title(self, title=None) -> bool:
        return title in self.drinks

    def get_drinks_sorted_by_title(self) -> list:
        return list(dict(sorted(self.drinks.items())).values())

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        def check_date(pair) -> bool:
            key, value = pair
            return from_date <= value.production_date <= to_date;

        return list(dict(filter(check_date, self.drinks.items())).values())
