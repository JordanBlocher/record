#! /usr/bin/env python

from time import sleep
from threading import Thread

#from audio import capture, capture_stop
import audio

class Audio(Thread):

    def __init__(self, filename):
        Thread.__init__(self)
        self._filename = filename

    def run(self):
        audio.capture(self._filename)

    def stop(self):
        audio.capture_stop()

a = Audio("c.wav")
a.start()
try:
    while 1:
        sleep(0.1)
finally:
    a.stop()
