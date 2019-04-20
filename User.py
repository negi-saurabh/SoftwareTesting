class User:
	
	def __init__(self, name):
		self.name = name
		self.life = 6 #amount of lives the user have in the game equivalent to head,body,two arms, two legs in drawing of hangman
		self.guesses = [] #List that will contain user's guesses
		self.correctGuesses = 0 #number of correct Guesses of the user
	