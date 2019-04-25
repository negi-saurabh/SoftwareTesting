from Word import Word
from User import User
from Hangman import Hangman

#main function of the entire game that will execute everything
def main():

	again= "a"# variable to check if the user wants to play another game
	
	while(again != "q"):
		w = Word()
		h = Hangman()
		print("Welcome to hangman game!\n")#Welcome message
		
		user = User(input("Please enter your name\n"))
		
		print(w.selectedWord)
		
		print("Hello "+ user.name+", the word you need to guess has "+str(len(w.selectedWord))+" letters: ",end='')#message to tell the user the number of letter of the word he have to guess
		showGuessPosition(user.guesses,w.selectedWord)
		
		h.drawHangman(user.life)
		
		
		#Loop to keep going until user wins or he runs our of lives
		while(user.life > 0 and user.correctGuesses != len(set(w.selectedWord.casefold()))):
		
			guess = input("Enter your guess, you have "+str(user.life)+" chances left:\n")
			
			if((len(guess)==1)):#check if guess entered is one character
				if(((ord(guess) >= 65 and ord(guess) <=90) or (ord(guess)>=97 and ord(guess) <=122))):#allow only english alphabets
					if(guess.casefold() in w.selectedWord.casefold() and guess.casefold() not in user.guesses):#check if the guess is part of the word the user need to guess
					
						user.correctGuesses+=1 #increment correct guesses
						user.guesses.append(guess.casefold())#add the guess to the list
						showGuessPosition(user.guesses,w.selectedWord)#show the position of the guessed letter
					else:
						#if statement to check if the guess is repeated or if it is not part of the word
						if(guess.casefold() in w.selectedWord.casefold() and guess.casefold() in user.guesses):
							print("You have already correctly guessed the letter '"+guess+"' and it is part of the word\n") #if letter is correctly repeated lives is not deducted
							
						elif(guess.casefold() not in w.selectedWord.casefold() and guess.casefold() in user.guesses):
							print("YOU HAVE ALREADY GUESSED THE LETTER '"+guess+"' AND IT IS NOT PART OF THE WORD")#if letter is repeated and it is not part of the word, then life is deducted
							user.life-=1#decrement the lives of the user
							h.drawHangman(user.life)#call method to add a drawing to the hangman
							
						else:
							print("Wrong letter!\n")#if the letter is guessed for the first time and it is not part of the word
							user.life-=1#decrement the lives of the user
							h.drawHangman(user.life)#call method to add a drawing to the hangman
						
						user.guesses.append(guess)
						
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
		
		again = input("\nEnter q to exit or enter anything else to play another game\n").casefold()
			
#method that will display the guessed letter if it is in the word
def showGuessPosition(guesses,word):
	for i in word.casefold():
		if i in guesses:
			print(i,end='')
		else:
			print("-",end='')
	print()
main()