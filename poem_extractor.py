import synonyms
import re
import sys

def make_title(query, debug=False):

	#Break the Poem in to words
	matches = re.findall('[a-zA-Z]+', query)
	refined = [match.lower() for match in matches]

	print set(refined)

	result = []

	#Get its synonyms
	for word in set(refined):
		try:
			result += synonyms.get_synonyms(word)
		except:
			continue
		if debug:
			print 'query : {query} \n result : {result}\n\n'.format(query=word, result=result)

	maxcounted_words = []
	maxcount   = 0

	#Calculate its occurence and return the max occurence
	for word in result:
		try:
			count=result.count(word)
			if count>maxcount:
				maxcount = count
				maxcounted_words = [word]
			elif count==maxcount:
				maxcounted_words.append(word)
			if debug:
				print 'Synonym : \"{word}\" and its occurence : {count}'.format(word=word, count=count)
		except:
			pass

	return (set(maxcounted_words), maxcount)

if __name__ == '__main__':
	query = open(sys.argv[1], 'r').read()
	result = make_title(query, True)
	print '\n\n'
	for word in result[0]:
		print 'Matched Result : {}'.format(word)
