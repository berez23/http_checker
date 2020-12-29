import time
import csv
from datetime import datetime
import requests


def check_status(url):

    while True:
        r = requests.get(url, timeout=15)
        status = r.status_code
        nows = datetime.now()
        ipsorgente = requests.get("https://checkip.amazonaws.com").text.strip()
        elapse = r.elapsed
        with open("status.csv", mode="a") as file:
            writers = csv.writer(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writers.writerow([nows, status, elapse, ipsorgente])
        time.sleep(2)


check_status("https://www.example.org")
