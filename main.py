import pyttsx3

text = 'Hello,this is a text to speech conversion example.'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

engine.save_to_file(text, 'my.mp3')
engine.runAndWait()

print("Saved as my.mp3")
