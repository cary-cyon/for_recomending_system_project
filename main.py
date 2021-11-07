# This is a sample Python script.

import librosa
from Array_of_features_create import return_features_array
audio_data = 'Violet.mp3'

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    # src = "forest floor.mp3"
    # dst = "forest floor.wav"
    #
    # # convert wav to mp3
    # sound = AudioSegment.from_mp3(src)
    # sound.export(dst, format="wav")
    #
    print("Start Openning")
    x, sr = librosa.load(audio_data)
    print("End Openning")
    arr = return_features_array(x, sr)
    print(arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
