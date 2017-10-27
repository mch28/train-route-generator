import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
announcement = 'This is the train to... Horton Buxley. Serving, Dibbon Town, Fennington Brin, Wensleyford, Dibbon Rake, Wawlend, Wensleyford Sutton... and Horton Buxley... The next stop, is Dibbon Rake'

engine.say(announcement)
engine.runAndWait()