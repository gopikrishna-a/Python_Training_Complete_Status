


mydict = {'beautiful': 'attractive','funny': 'humorous','happy': 'joyfull'}
word = raw_input("Enter Ur Word for Synonym (Lower Case Only):")



if word in mydict:
	print "Synonyms for "+word+ " are",(mydict[word])
else:
	print "Sorry Word not fount"
	syn  = raw_input("Enter Synonym of Ur Word To add :")
	mydict[word] = syn #adding new key and value to Dictonary
	print mydict
	
