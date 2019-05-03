import random

class Word:
	
	words = ["Apple","Orange","School","Apartment","University","Car","fee","oil","hangman","experiment"]
	def __init__(self):
		self.selectedWord = self.chooseWord()
	
	#This function will return a random word from the list of words
	def chooseWord(self):
		return random.choice(self.words)