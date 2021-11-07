import librosa
import numpy as np
def return_features_array(file, sr):
    featurse = {"spectral_centroid": librosa.feature.spectral_centroid(file, sr=sr),
                "zero_crosing": librosa.feature.zero_crossing_rate(file, pad=False).sum()}
    return featurse
