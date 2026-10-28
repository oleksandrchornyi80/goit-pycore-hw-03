import datetime
def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.date.today()
        difference = current_date - given_date
        return difference.days
    except ValueError:
           raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
