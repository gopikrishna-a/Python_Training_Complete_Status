#Created By A.Gopikrishna on 25/01/2017
#Python 2.7.3
#Printing Synonym For User input word Using Class and Defination

class Synonyms(object):

	def __init__(self):
		self.mydict = {'beautiful': 'attractive','funny': 'humorous','happy': 'joyfull'}
		self.word = raw_input("Enter Ur Word for Synonym (Lower Case Only):")


	def find_syn(self):
		if self.word in self.mydict:
			print "Synonyms for "+self.word+ " are",(self.mydict[self.word])

		else:
			print "Sorry Word not fount"
			self.syn  = raw_input("Enter Synonym of Ur Word To add :")
			self.mydict[self.word] = self.syn #adding new key and value to Dictonary
			print self.mydict



a = Synonyms()
a.find_syn()





	

		




	

















	

