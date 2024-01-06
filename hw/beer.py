from datetime import date

class Beer:

    def __init__(self, title=str, production_date=date) -> None:
        self.title = title
        self.production_date = production_date

    def __repr__(self) -> str:
        return f'Beer[title:{self.title}, production_date={self.production_date}'
