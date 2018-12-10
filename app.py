from mingus.midi import fluidsynth
from mingus.containers import Note, NoteContainer
import time

SF2 = '/home/btc/Escritorio/SinestesiaRCB/gfx/FluidR3_GM.sf2'

if not fluidsynth.init(SF2, 'alsa'):
    print "Couldn't load soundfont: ", SF2
    sys.exit(1)
else:
    print "SF2 loaded"

n = Note("C-5")
n.channel = 0
n.velocity = 50
c = 0

while c != "false":
    fluidsynth.play_Note(n)
    time.sleep( 0.5 )
    fluidsynth.stop_Note(n)
    c = raw_input("Introduce false si quieres acabar: ")
