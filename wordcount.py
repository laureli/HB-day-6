from sys import argv

script, from_file = argv

text = open(from_file)
book = text.read()
book = book.lower()

text.close()
words=""
for letter in book:
	if ord(letter)<ord('a') or ord(letter)>ord('z'):
		letter=letter.replace(letter,' ') 
	words=words+letter
	
words = words.split()


word_count={}
for item in words:
	current_count=word_count.setdefault(item,0)
	current_count+=1
	word_count[item]=current_count


for i,j in word_count.iteritems():
	print i,j
