from logger import methods_logger

@methods_logger
class Market:

    def __init__(self, wines: list = None, beers: list = None) -> None:
        drinks_list = ([] if wines is None else wines) + ([] if beers is None else beers)
        self.drinks = dict((d.title, d) for d in drinks_list)

    def has_drink_with_title(self, title=None) -> bool:
        return title in self.drinks

    def get_drinks_sorted_by_title(self) -> list:
        return list(dict(sorted(self.drinks.items(), key = lambda k: (k[0] is None, k[0]))).values())

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        def check_date(pair) -> bool:
            key, value = pair
            if value.production_date is None:
                return False; 
            return from_date <= value.production_date and (to_date is None or value.production_date <= to_date);
    
        if from_date is None:
            return list(self.drinks)
        return list(dict(filter(check_date, self.drinks.items())).values())
