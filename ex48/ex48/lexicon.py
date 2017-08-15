def scan(sentence):
	words = sentence.split()
	converted_sentence = []
	for word in words:
		converted_word=identify_word(word)
		converted_sentence.append(converted_word)
	return converted_sentence
	
def identify_word(word):
	adj_word=word.lower()
	if adj_word in ['north','south','east','west']:
		return ('direction',adj_word)
	elif adj_word in ['go', 'kill', 'eat']:
		return ('verb',adj_word)
	elif adj_word in ['the', 'in', 'of']:
		return ('stop',adj_word)
	elif adj_word in ['bear','princess']:
		return ('noun',adj_word)
	try:
		return ('number',int(word))
	except ValueError:
		return ('error',word)
