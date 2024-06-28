# johannes joujo jag tog koden från länken under och ändrade på den så att den
# ska uppfylla kraven som Jimmy Åhlander ställde
# Torsdag 8 december 2022 klockan 20:25:15
# Ändrade på koden Fredag 13 Januari 14:15 2023

# https://codezup.com/python-program-reader-writer-problem-mutex/

from datetime import datetime
import threading as thread

global x  # Shared Data
x = 0
lock = thread.Lock()  # Lock for synchronising access
sema = thread.Semaphore(3)
antal_sema = sema._value


def acrall():
    for i in range(antal_sema):
        sema.acquire()


def reliceall():
    for i in range(antal_sema):
        sema.release()


def Reader():
    global x
    while True:
        if True == lock.locked():
            pass
            #print('Reader is Waiting!!!!!!!!!!!!!!!!!!')
        else:
            sema.acquire()  # Acquire the lock before Reading (mutex approach)
            print('Reader is Reading!')
            print('Shared Data:', x)
            print("Reader reliced lock\n")
            sema.release()  # Release the lock after Reading
            print()


def Writer():
    global x
    while True:
        lock.acquire()  # Acquire the lock before Writing
        acrall()
        x = datetime.now().strftime("%D %X \n")  # Write on the shared memory
        print('Writer is Writing!-------------------------------------')
        reliceall()
        print("Writer reliced lock------------------------------------")
        lock.release()  # Release the lock after Writing
        print()


def ReverseWriter():
    global x
    while True:
        lock.acquire()  # Acquire the lock before Writing
        acrall()
        x = datetime.now().strftime("%D %X \n")[
            ::-1]  # Write on the shared memory
        print('ReverseWriter is Writing!------------------------------------')
        reliceall()
        print("ReverseWriter reliced lock------------------------------------")
        lock.release()  # Release the lock after Writing
        print()


Thread1 = thread.Thread(target=Reader)
Thread2 = thread.Thread(target=Writer)
Thread3 = thread.Thread(target=ReverseWriter)
Thread4 = thread.Thread(target=Reader)
Thread5 = thread.Thread(target=Reader)
Thread6 = thread.Thread(target=Reader)


Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()
Thread5.start()
Thread6.start()
