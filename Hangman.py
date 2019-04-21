class Hangman:
	
	def __init__(self):
		self.hangmanDrawing = ["","","","","",""]

	
	#this method will add a part to the hangman drawing each time the user guesses a wrong letter
	def drawHangman(self,lives):
		
		#if else if statements to add the appropriate part of the drawing depending the lives of the user left
		if(lives==5):
			self.hangmanDrawing[0]="O"
		elif(lives == 4):
			self.hangmanDrawing[1]="|"
		elif(lives == 3):
			self.hangmanDrawing[2]="/"
		elif(lives == 2):
			self.hangmanDrawing[3]= "\\"
		elif(lives == 1):
			self.hangmanDrawing[4]= "/"
		elif(lives == 0):
			self.hangmanDrawing[5]= "\\"
		
		#print statement that actually prints the drawing
		print("------\n"+str("|").ljust(5)+"|\n"+str("|").ljust(5)+self.hangmanDrawing[0]+"\n"+str("|").ljust(4)+self.hangmanDrawing[2].ljust(1)
		+self.hangmanDrawing[1]+self.hangmanDrawing[3]+"\n"+str("|").ljust(4)+self.hangmanDrawing[4].ljust(2)+self.hangmanDrawing[5]+"\n-")
	