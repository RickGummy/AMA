import subprocess
import time

sf2_path = "FluidR3_GM.sf2"
midi_path = "mozart.mid"

process = subprocess.Popen([
    "fluidsynth",
    "-i",
    sf2_path,
    midi_path
])

time.sleep(30)

process.terminate()