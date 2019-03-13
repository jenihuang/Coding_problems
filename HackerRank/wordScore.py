
#start a score count per word
#start a final score
#for word in words, count the vowels
#if count mod 2 is 0, then final += 2, else 1

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
	wordList = words.split()
	score = 0
	for word in wordList:
		num_vowels = 0
		for letter in word:
			if is_vowel(letter):
				num_vowels += 1
		if num_vowels % 2 == 0:
			score += 2
		else:
			score += 1

	return score



print(score_words("programming is awesome"))