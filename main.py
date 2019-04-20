from Word import Word
from User import User

#main function of the entire game that will execute everything
def main():
	w = Word()
	selectedWord = w.chooseWord() #this variable will contain the selected word
	
	print("Welcome to hangman game!\n")#Welcome message
	
	user = User(input("Please enter your name\n"))
	
	print(selectedWord)
	
	print("Hello "+ user.name+", the word you need to guess has "+str(len(selectedWord))+" letters\n")#message to tell the user the number of letter of the word he have to guess
	showGuessPosition(user.guesses,selectedWord)
	
	
	#Loop to keep going until user wins or he runs our of lives
	while(user.life > 0 and user.guessedWord == False):
	
		guess = input("Enter your guess, you have "+str(user.life)+" chances left:\n")
		
		if((len(guess)==1)):
			if(((ord(guess) >= 65 and ord(guess) <=90) or (ord(guess)>=97 and ord(guess) <=122))):
				if(guess in selectedWord):
					user.guesses.append(guess)
					showGuessPosition(user.guesses,selectedWord)
			else:
				print("Please enter an English letter")
		else:
			print("Please enter a single English letter")
			
#method that will display the guessed letter if it is in the word
def showGuessPosition(guesses,word):
	for i in word:
		if i in guesses:
			print(i,end='')
		else:
			print("-",end='')
	print()
main()