import mido

midi_path = "mozart.mid"

mid = mido.MidiFile(midi_path)

for i, track in enumerate(mid.tracks):
    print(f"Track {i}: {track.name}")
    for msg in track:
        print(msg)