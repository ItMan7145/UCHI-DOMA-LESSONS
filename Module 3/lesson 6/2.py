import datetime as dt
import time

import schedule


def ura_new_year():
    data_now = dt.datetime.now()
    data_new_year = dt.datetime(2024, 1, 1)

    delta = data_new_year - data_now

    print(
        f"До нового года осталось дней: {delta.days}, часов: {delta.seconds // 3600}, минут: {(delta.seconds // 60) % 60}, секунд: {delta.seconds % 60}")


schedule.every(1).seconds.do(ura_new_year)
while 1:
    schedule.run_pending()
    time.sleep(1)
