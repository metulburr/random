import time
import threading

class MyThread(threading.Thread):

    def __init__(self):
        self._should_stop = threading.Event()
        threading.Thread.__init__(self)

    def run(self):
        while not self._should_stop.is_set():
            # Do stuff
            print('thread running')
            time.sleep(1)
        self._should_stop.clear()

    def stop(self):
        self._should_stop.set()
        while self._should_stop.is_set():
            time.sleep(1)


t = MyThread()
t.start()
print('running main')
time.sleep(3) # Do something until it's time to terminate
assert threading.active_count() == 2
t.stop()
print('thread stop')
assert threading.active_count() == 1
