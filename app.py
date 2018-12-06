from mingus.midi import fluidsynth

fluidsynth.init('/home/btc/Escritorio/DockerImages/Synesthesia/gfx/dani.opus',"alsa")

fluidsynth.play_Note(64,0,100)