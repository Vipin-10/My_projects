import gtts
import os
mytext="Success is not final failure is not fatal It is the courage to continue that counts"
language='en'
output= gtts.gTTS(text=mytext, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")