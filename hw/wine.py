from drink import Drink

class Wine(Drink):

    def __init__(self, title=None, production_date=None) -> None:
        super().__init__(title, production_date)

    def __repr__(self) -> str:
        return f'Wine[title:{self.title}, production_date={self.production_date}'
