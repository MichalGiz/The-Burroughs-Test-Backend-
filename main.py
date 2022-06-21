
import json
import datetime
import calendar

from typing import Union
from fastapi import FastAPI

DATA = None


def initialize_data():
    """ Read data from data.json file, file can be generated with generate_empl.py tool """
    global DATA
    with open("data.json") as f:
        DATA = json.load(f)

def initialize_db():
    """ Initialize DB, for testing it is only json file, later on can be real DB """
    initialize_data()

initialize_db()


app = FastAPI()


@app.get("/list")
def list_employees():
    return DATA

@app.get("/salaries/{querydate}")
def list_salaries(querydate: Union[str, None] = None):
    try:
        date_time_obj = datetime.datetime.strptime(querydate, '%Y-%m-%d')
    except ValueError:
        return {"error": "Bad date format - provide YYYY-MM-DD"}
    startmonth = date_time_obj.month
    startyear = date_time_obj.year if startmonth < 12 else date_time_obj.year + 1
    startmonth = startmonth + 1 if startmonth < 12 else 1
    dates = []
    for m in range(12):
        current_date = datetime.date(startyear, startmonth, 1)
        payday = current_date - datetime.timedelta(days=1)
        if payday.weekday() in [5, 6]:
            payday = payday + datetime.timedelta(days=(7 - payday.weekday()))
        bonusdate = current_date + datetime.timedelta(days=14)
        if bonusdate.weekday() in [5, 6]:
            bonusdate = bonusdate + datetime.timedelta(days=(7 - bonusdate.weekday() + 2))
        startmonth += 1
        if startmonth > 12:
            startmonth = 1
            startyear += 1
        dates.append({'payday': payday, 'bonus': bonusdate})
    result = []
    for d in dates:
        for e in DATA:
            result.append({'day': str(d['payday']), 'type': 'SALARY', 'id': e['id'], 'first_name': e['first_name'],
                'last_name': e['last_name'], 'amount': e['salary']})
            result.append({'day': str(d['payday']), 'type': 'BONUS', 'id': e['id'], 'first_name': e['first_name'],
                'last_name': e['last_name'], 'amount': int(e['salary'] / 100 * e['perc_bonus'])})
    return result

