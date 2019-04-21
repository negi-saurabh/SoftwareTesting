from Word import Word
from User import User
from Hangman import Hangman

#main function of the entire game that will execute everything
def main():
	w = Word()
	h = Hangman()
	
	print("Welcome to hangman game!\n")#Welcome message
	
	user = User(input("Please enter your name\n"))
	
	print(w.selectedWord)
	
	print("Hello "+ user.name+", the word you need to guess has "+str(len(w.selectedWord))+" letters: ",end='')#message to tell the user the number of letter of the word he have to guess
	showGuessPosition(user.guesses,w.selectedWord)
	
	h.drawHangman(user.life)
	
	
	#Loop to keep going until user wins or he runs our of lives
	while(user.life > 0 and user.correctGuesses != len(set(w.selectedWord))):
	
		guess = input("Enter your guess, you have "+str(user.life)+" chances left:\n")
		
		if((len(guess)==1)):#check if guess entered is one character
			if(((ord(guess) >= 65 and ord(guess) <=90) or (ord(guess)>=97 and ord(guess) <=122))):#allow only english alphabets
				if(guess.casefold() in w.selectedWord.casefold()):#check if the guess is part of the word the user need to guess
				
					user.correctGuesses+=1 #increment correct guesses
					user.guesses.append(guess.casefold())#add the guess to the list
					showGuessPosition(user.guesses,w.selectedWord)#show the position of the guessed letter
				else:
					print("Wrong letter!\n")
					user.guesses.append(guess)
					user.life-=1#decrement the lives of the user
					h.drawHangman(user.life)#call method to add a drawing to the hangman
			else:
				print("Please enter an English letter")
		else:
			print("Please enter a single English letter")
	
	if(user.life == 0):#message if the user loses
		print("\nYou've been hanged! The correct word was: "+w.selectedWord+"\n")
		
	else:#if they win
		print("\nYou Win !\n")
	
	print("You have made "+str(len(user.guesses))+" guesses in this game which are:")
	
	#print all user guesses
	for i in user.guesses:
		print(i+", ",end='')
			
#method that will display the guessed letter if it is in the word
def showGuessPosition(guesses,word):
	for i in word.casefold():
		if i in guesses:
			print(i,end='')
		else:
			print("-",end='')
	print()
main()