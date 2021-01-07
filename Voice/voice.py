
from gtts import gTTS 


import os 


mytext = 'Welcome to Cojag!'


language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False) 


myobj.save("cojag.mp3") 

 
os.system("mpg321 welcome.mp3")
