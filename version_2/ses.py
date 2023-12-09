#anlaşılabilir olan  sesi buradan seçiyorum  
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id) #[i] i'yi değiştirebilirsin


engine.say('ikinci') #ikinci kelimesini okur.
engine.runAndWait()

