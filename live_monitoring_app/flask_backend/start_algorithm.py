import sys
from threading import Thread

runAlgo = True

def startAlgo():
    global runAlgo
    runAlgo = True
    while runAlgo:
        print(runAlgo)


def stopAlgo():
    global runAlgo
    runAlgo = False
    print("algorithm stop called")