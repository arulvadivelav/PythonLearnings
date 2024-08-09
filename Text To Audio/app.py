# =============================================================== #
#   Text to speech convertor using gTTs (Goolgle Text To Speech)  #
# =============================================================== #

# pip install gtts

from gtts import gTTS
import os, easygui

# Using easygui to open the file location
input_file = easygui.fileopenbox()

# read the input text file to convert into audio
input_text = ""
with open(input_file, "r", encoding="utf-8") as file:
    for text in file:
        input_text += text

# gTTs Class call for the process

# text - Input text from the given file
# lang - To set the audio language(ex: en - english, ta - tamil)
# slow - To set audio speed

output = gTTS(text=input_text, lang="ta", slow=False)

# Using easygui to get the file location to save
output_file = easygui.filesavebox()
output.save(output_file)

# Usibg os to automatically play the downloaded audio
os.system("start audio.mp3")
