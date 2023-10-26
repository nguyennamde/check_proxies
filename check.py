import threading
import queue
import requests

q = queue.Queue()

with open("list_proxy_free.txt", mode="r") as f:
    list_proxies = f.read().split("\n")
    for proxy in list_proxies:
        q.put(proxy)

def check_proxies():
    global q
    while not q.empty():
        try:
            proxy = q.get()
            res = requests.get("http://ipinfo.io/json",
                               proxies={
                                   'http' : proxy,
                                   'https' : proxy
                               })
        except:
            continue
        if res.status_code == 200:
            print(proxy)

threads = []
for _ in range(10):
    thread = threading.Thread(target=check_proxies)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
