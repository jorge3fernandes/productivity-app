from datetime import date, timedelta
import pandas as pd


def getWeek(input_date):
    week_day = input_date.isocalendar()[2]
    print(week_day)
    if week_day == 7:
        week_start = input_date
        week_end = week_start + timedelta(days=6)
        return [week_start, week_end]
    else:
        week_start = input_date - timedelta(days=input_date.weekday()+1)
        week_end = week_start + timedelta(days=6)
        return [week_start, week_end]


def generateDays(start_date, end_date, freq):
    return pd.date_range(start_date, end_date, freq=freq)
