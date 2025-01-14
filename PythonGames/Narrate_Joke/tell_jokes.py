import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

## To change voice
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

with open('Jokes.db', 'r') as j_in:
    jokes = j_in.readlines()

for line in jokes:
    engine.say(line)
    engine.runAndWait()