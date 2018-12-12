#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import socket
from mingus.midi import fluidsynth
from mingus.containers import Note

SF2 = '/home/btc/Escritorio/SinestesiaRCB/gfx/FluidR3_GM.sf2'

if not fluidsynth.init(SF2, 'alsa'):
    print "Couldn't load soundfont: ", SF2
    sys.exit(1)
else:
    print "SF2 loaded"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if not s:
    print "Couldn't create UDP socket"
else:
    port = 50288
    s.bind(("", port))
    print "UDP socket ready"

data = 0

while data != "end":
    try:
        data, addr = s.recvfrom(1024)
        numero = int(str(data))
        print "Tecla: " + str(data)
        fluidsynth.play_Note(20 + (5*int(numero)),0,120)

    except Exception as e:
        if str(data) != "end":
            print(e)
