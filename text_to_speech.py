### Made by Tristan Starkl L'immortel
## Propriété de Thomas Rety

from gtts import gTTS
import os


class textToSpeech():
	def __init__(self):
		pass

	def say(self, text2):
		tts = gTTS(text=text2, lang="fr", slow=False)
		tts.save('./temp/good.mp3')


	def speak(self):
		os.system("mpg321 --stereo ./temp/good.mp3")


class livre():
	def __init__(self, name):
		self.name = name
		self.tts = textToSpeech()

	def read(self):
		with open(self.name, 'r') as f:
			lines = f.readlines()
			for line in lines:
				self.tts.say(line)
				self.tts.speak()



l = livre("./livres/eragon.json")

l.read()