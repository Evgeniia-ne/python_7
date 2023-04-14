import time


class TraficLigth:

    __color = "red"


    def running(c):
        while c > 0:
            color = "red"
            print(color)
            time.sleep(7)
            color = "yellow"
            print(color)
            time.sleep(2)
            color = "green"
            print(color)
            time.sleep(5)
            c = c-1


a = TraficLigth.running
a(2)