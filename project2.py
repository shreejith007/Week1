import pyttsx3
import wikipedia
voice = pyttsx3.init()
In=input(" SEARCH:-")

result =wikipedia.summary(In ,sentences = 3)
print (result)
voice.say(result)
voice.say(result)
voice.runAndWait()