import getpass
import movieread
import pickle
import random
class User:
	def __init__(self):
		pass
	def input(self):
		self.name=input()
		self.password=getpass.getpass()
		admin=False
	def getmovielist(self):
		try:
			with open("pymovies.pkl","rb") as file:
					movielist=pickle.load(file)
			return (movielist)
		except IOError:
			return None
	def dispmovies(self,genre):
		movielist=self.getmovielist()
		
		if(movielist!=None):
			movielist.sort(key=movieread.movie_compare,reverse=True)
			i=0
			while(i<6):
				try:
					if(movielist[i].overall_genre==genre):
						print(movielist[i])
						i+=1
				except Exception:
					print("OUT OF MOVIES")
	

		

	def Options(self):
		while True:
			if(i==0):
				break
			if(i==1):
				self.dispmovies("action",0)
			if(i==2):
				print(self.getmovielist())


class Admin(User):
	def __init__(self):
		super().__init__()
	admin=True

	def createmovielist(self):
		while True:
			p=movieread.movie()
			p.input()
			try:
				with open("pymovies.pkl","rb") as file:
					movielist=pickle.load(file)
					p.id=len(movielist)+1
					movielist.append(p)
			except IOError:
				p.id=1
				movielist=[p]
			with open("pymovies.pkl","wb") as file:
				pickle.dump(movielist,file,pickle.HIGHEST_PROTOCOL)
			break


	def generaterandom(self):
		movielist=[]
		for i in range(100):
			p=movieread.movie()
			p.id=i
			for i in range(len(p.genre_list)):
				p.genre_rating[i]=random.random()*10
			p.release_year=random.randint(1950,2010)
			p.rating_overall=random.random()*10
			strt=""
			for i in range(6):
				strt+=chr(random.randint(1,26))
			p.name=strt
			p.overall_genre=
			print(sorted(p.genre_rating))
			movielist.append(p)
		return (movielist)

	def Options(self):
		i=input()
		if(i==0):
			self.createmovielist()
		if(i==1):
			self.generaterandom()