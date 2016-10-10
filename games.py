import random

def playMysteryNumberGame(friend_number, out_number):
	'''I'm thinking of a number. I'll tell you what that number plus or minus another number 	equals'''
	print '%d plus your mystery number equals %d... I\'m thinking' % (friend_number, out_number)
	#1 + 2 = 3, 3 - 2 = 1: a+b=c == c-a=b	
	mystery_number = out_number - friend_number 
	print 'Aha! Your mystery number must be %d' % mystery_number

def rememberMysteryNumber(friend_number, out_number):
	'''Play the mystery number game, then remember that number'''
	mystery_number = out_number - friend_number
	return(mystery_number)

def playGreenGlassDoor():
	'''What can go through the green glass door? Three options, tell me which can!'''
	objects = {"Acorn":"1", "Bicycle":"2", "Wheel":"3"}
	for key in objects:
		print objects[key] + '. ' + key	
	answer = input('What can go through the green glass door?')	

def playZebraWord(word):
	'''Given a word, this will tell you if it is a zebra word (any word that ends with the 		same two consonants'''
	word = word.strip()
	if type(word) == str:
		if word[len(word)-2] == word[len(word)-1]:
			print 'Yup! That is a zebra word!' 
		else: 
			print 'No, doesn\'t look like one'
	else:
		print 'Hey, that\'s not a word!'

def playGuessANumber(start, end, tries):
	'''Pick a random number between the start and the end numbers, and give you tries to guess 		the number.'''
	picked_number = random.randrange(start, end)
	print 'Let\'s play a guessing game. I\'m thinking of a number between %d and %d. You have %d guesses!' % (start, end, tries)
	i = 0	
	while i < 1:
		answer = input('Guess a number!')
		if answer == picked_number:
			print 'You got it right!'
		else:
			i += 1
	while i < tries:
		answer = input('Guess again')
		if answer == picked_number:
			print 'You got it right!'
		else:
			i += 1
			print 'Nah, not right'
	print 'I win! The answer was %d' % picked_number

	 
