import librosa
import numpy as np
import tensorflow as tf
import argparse
import json
# Input dimension for model = 259*13

mappings = ["blues","classical","country","disco","hip-hop","jazz","metal","pop","reggae","rock"]
model_path = "Base_CNN_classifier.h5"
def preprocess_audio(file_path, target_frames=259, n_mfcc=13, sr=22050, n_fft=2048, hop_length=512):
    # Load audio file
    y, sr = librosa.load(file_path, sr=sr)

    # Compute MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    # Pad or truncate MFCCs to ensure they have target_frames
    if mfccs.shape[1] < target_frames:
        pad_width = target_frames - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfccs = mfccs[:, :target_frames]
    return mfccs.T

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

def run_inference(model, input_data):
    input_data = input_data[np.newaxis, ...]
    predictions = model.predict(input_data)
    return predictions

# model = load_model(model_path)
# input_data = preprocess_audio("metal.00003.wav")
# predictions = run_inference(model, input_data)
# text_predictions = [mappings[np.argmax(predictions, axis=1)[0]]]
# with open("output.json", 'w') as f:
#     json.dump(text_predictions, f)

def main():
    parser = argparse.ArgumentParser(description='Run inference on a TensorFlow model.')
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input data JSON file.')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the inference results.')

    args = parser.parse_args()
    model = load_model(model_path)
    input_data = preprocess_audio("metal.00003.wav")
    predictions = run_inference(model, input_data)
    text_predictions = list[mappings[np.argmax(predictions, axis=1)[0]]]
    with open(args.output_path, 'w') as f:
        json.dump(text_predictions, f)

    print(f'Inference results saved to {args.output_path}')

if __name__ == '__main__':
    main()