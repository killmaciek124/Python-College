from threading import Thread
from time import sleep, ctime

MAX_WIEK_KOTA = 10
wiek_kota = 0


class Timer(Thread):
    def __init__(self, time, target):
        Thread.__init__(self)
        self.time = time
        self.target = target
        self.start()

    def run(self):
        while self.target():
            sleep(self.time)


def dodaj_jeden_do_wieku_kota():
    global wiek_kota
    if wiek_kota < MAX_WIEK_KOTA:
        if wiek_kota == 0:
            msg = '%s: narodziny kota' % ctime()
        else:
            msg = '%s: urodziny kota, kot skończył %i lat' % (ctime(), wiek_kota)
            print(msg)
            wiek_kota += 1
            return True
            print('kot umarł ze starości w wieku %i lat' % wiek_kota)


def test():
    Timer(2, dodaj_jeden_do_wieku_kota)


if __name__ == '__main__':
    test()
