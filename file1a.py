import time
import os

def clock():
    time0 = round(time.time())
    while True:
        if (round(time.time()) - time0) % 5 == 0:
            yield "5 sec"
        else:
            yield 0
            
            
            
def query():
    for i in os.walk("C:\\"):
        yield i[0]  # Вот здесь функция стала генератором, благодаря оператору yield
        

def main():
    data = query() #  data стала генератором
    alarm = clock()
    while True:
        d = next(data)
        a = next(alarm)
        print(d)
        if a: print(a)
        time.sleep(1)
main()