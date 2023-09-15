# Text To Speech
This is a Python program that converts a text file into speech.

## Prerequisites

The Python script requires following:

- Python version: Python 3.x
- gTTS library: [gTTS (Google Text-to-Speech) library](https://pypi.org/project/gTTS/)
- playsound library: [playsound](https://pypi.org/project/playsound/)
- A text file: Containing the text which is needed to be converted into audio.

You can install the gTTS library using pip:

```
pip install gTTS
```

You can install the playsound library using pip:

```
pip install playsound
```

## Usage

1. The ```audio``` variable that stores a audio file named 'speech.mp3'.
2. The ```language``` variable defines which language the audio should be using. Here we used Hindi as 'hi'.
3. The ```text_file_path``` variable stores the text file.
4. In order to read the content present inside the text file, the file is opened, read and stored in the variable ```text_content```.
5. The ```gTTS()``` method is called which has parameters 'text' which accepts the 'text_content', 'lang' accepts 'language', 'slow' which accepts boolean value 'True' or 'False'.
6. The ```save()``` method will create and save the final mp3 file in speech.mp3.
7. ```playsound()``` will then play the audio through default audio application installed in your system.

## Configuration

You can customize the following parameters in the script:

- text_file_path: Path to the input text file. You can change the content of the file as per your requirments.
- language: The language of the text (e.g., 'en' for English, 'ja' for Japanese).
- slow: Set to True if you want the speech to be generated slowly.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
