import librosa

class _Beat_tracking_service():
    instance = None
    def get_beat(self,file_path):
        y, sr = librosa.load(file_path)
        beat = librosa.beat.beat_track(y=y, sr=sr)
        return beat[0][0]

def Beat_tracking_service():
    if _Beat_tracking_service.instance == None:
        _Beat_tracking_service.instance = _Beat_tracking_service()
    return _Beat_tracking_service.instance

if __name__ == "__main__":
    emotion_service = Beat_tracking_service()
    predicted_beat = emotion_service.get_beat("10.mp3")
    print(predicted_beat)