text_file=open("scores.txt")

score_dict={}

for line in text_file:
  line=line.split(":")
	score_dict[line[0]]=int(line[1])
text_file.close()

def play():
	while True:
		entry = raw_input('For sort by name, enter name.  \nFor sort by score, enter score.\n"quit" to quit \n->' )
		if entry == 'name':
			return sorted_names()

		elif entry == 'score':
			return sorted_scores()

		elif entry == 'quit':
			break

		else:
			print 'please type the right thing'
			entry = raw_input('please type score or name -> ')

def sorted_names():
	keys_score_dict= sorted(score_dict) 
	for i in keys_score_dict:
		print "Restaurant",i,"is rated at",str(score_dict[i]) +"."
	play()

def sorted_scores():
	values_score_dict=sorted(score_dict,key=score_dict.get,reverse=True)
	for i in values_score_dict:
		print "Restaurant",str(i),"is rated at",str(score_dict[i])+"."
	play()


play()
