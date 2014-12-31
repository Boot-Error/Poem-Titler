import urllib
from bs4 import BeautifulSoup

#Method to get synonyms
def get_synonyms(query):

	#Website url to search with
	url = 'http://www.thesaurus.com/browse/{}'.format(query)
	#opening the website
	response = urllib.urlopen(url)
	document = BeautifulSoup(response.read())
	#Finding out the synonyms
	try:
		words = document.find('div', {'class' : 'relevancy-list'}).find_all('span', {'class':'text'})
	except:
		print 'synonyms for word \'{}\' not found'.format(query)

	return [word.string for word in words]

if __name__ == '__main__':
	query = 'the'
	for a in get_synonyms(query):
		print a