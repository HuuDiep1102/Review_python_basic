import requests
import time
from multiprocess import Queue
from threading import Thread
def request_func(urls, q):
    start_time_in = time.time()
    x = requests.get(url = urls)
    t = time.time() - start_time_in
    q.put({urls: t})
if __name__ == "__main__":
        start_time = time.time()
        URLS = ['https://docs.python.org/', 'https://realpython.com/', 'https://kaggle.com/', 'https://github.com/',
                'https://www.coursera.org/', 'https://trello.com/', 'https://www.sciencedirect.com/',
                'https://www.youtube.com/', 'https://bachasoftware.com/']
        dict = {}
        q = Queue()
        thread = [Thread(target=request_func, args=[urls, q, ]) for urls in URLS]
        for p in thread:
              p.start()
        for p in thread:
              p.join()
              dict.update(q.get())
        # Thoi gian chay chuong trinh
        print('Thoi gian chay tung thread')
        print(dict)
        print('Thoi gian chay chuong trinh {}'.format(time.time() - start_time))