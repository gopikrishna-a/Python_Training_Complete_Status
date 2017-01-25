#Created By A.Gopikrishna on 25/01/2017
#Python 2.7.3
#Printing Synonym For User input word


mydict = {'beautiful': 'attractive','funny': 'humorous','happy': 'joyfull'}#adding words into dictionary
word = raw_input("Enter Ur Word for Synonym (Lower Case Only):")#taking user input word

if word in mydict:
	print "Synonyms for "+word+ " are",(mydict[word])#printing the Synonym if word exists
else:
	print "Sorry Word not fount"
	syn  = raw_input("Enter Synonym of Ur Word To add :")
	mydict[word] = syn #adding new key and newword to Dictonary as it is not in the dictionary 
	print mydict
	
