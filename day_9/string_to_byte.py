import pickle


my_list = [1,2,3,4,5]
my_dict = {'name':'gopi'}
my_str = 'asm tech'
f = open('new.txt','w')
pickle.dump(my_list,f)
pickle.dump(my_dict,f)
f.close() 

