import schedule
import time

from runner_functions import get_quotes_and_clean



schedule.every().day.at("10:00").do(get_quotes_and_clean)

while True:
    schedule.run_pending()
    time.sleep(60)