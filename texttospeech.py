from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'hi'

text_file_path = 'Textfile.txt'

# Read the content of the text file
with open(text_file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

sp = gTTS(text=text_content, lang=language, slow=False)

sp.save(audio)
playsound(audio)