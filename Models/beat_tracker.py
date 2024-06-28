import librosa

def beat_getter(uploaded_file):
    y,sr = librosa.load(uploaded_file)
    beat = librosa.beat.beat_track(y=y,sr=sr)
    return beat

print(beat_getter("metal.00003.wav"))