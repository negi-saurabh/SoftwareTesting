import random

class Word:
	
	words = ["apple","orange","school","apartment"]
	
	#This function will return a random word from the list of words
	def chooseWord(self):
		return random.choice(self.words)