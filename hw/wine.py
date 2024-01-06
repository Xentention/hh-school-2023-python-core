from datetime import date

class Wine:

    def __init__(self, title=str, production_date=date) -> None:
        self.title = title
        self.production_date = production_date

    def __repr__(self) -> str:
        return f'Wine[title:{self.title}, production_date={self.production_date}'
