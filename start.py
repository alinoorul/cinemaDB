#start.py
import user
import pickle
def firstuse():
	t=user.Admin()		#Skipping user checking
	t.getmovielist()
	if t==None:
		movielist=t.generaterandom()
		try:
			with open("pymovies.pkl","wb") as file:
				pickle.dump(movielist,file,pickle.HIGHEST_PROTOCOL)
		except IOError:
			pass 
	print("USER(0)/ADMIN(1):",end=" ")
	p=input()
	if(p==0):
		t=user.User()
	t.Options()
firstuse()