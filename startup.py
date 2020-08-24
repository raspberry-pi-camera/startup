#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import os
from pathlib import Path
import sys

version = "1.0.0"

if len(sys.argv) > 1:
    if sys.argv[1] == "-v":
        print(version)
        exit()

try:
    os.environ['SSH_TTY']
    os.environ['SSH_CLIENT']
except KeyError:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    gui = GPIO.input(17)


    if not gui:
        env = os.environ
        env['LD_LIBRARY_PATH'] = "/opt/raspindi/usr/lib"
        subprocess.call('/opt/raspindi/bin/raspindi', env=env)
    else:
        with open("/tmp/neopixel.state", "w") as file:
            file.write("F")
        subprocess.Popen(['/opt/raspindi/bin/atem'])
        subprocess.call(['/usr/bin/raspistill', '-fp', '-t', '0', '-w', '1920',  '-h', '1080'])