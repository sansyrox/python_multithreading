from requests_futures.sessions import FuturesSession
import time
from requests import ConnectionError
import threading


def checker():
    session = FuturesSession()
    response_one = None
    while response_one is None:
        try:
            response_one = session.get('http://127.0.0.1:4000').result()
            print(response_one.status_code)
        except AttributeError:
            time.sleep(10)
            continue
        except ConnectionError:
            time.sleep(10)
            continue


t = threading.Thread(target=checker, name="Thread1")
# t.daemon = True
t.start()

print("Hello World")
print("Hello World")

t.join()


