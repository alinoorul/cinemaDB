import pickle 			1Q`
class movie:
	
	def __init__(self):
		self.genre_rating={}
		self.id=-1
		self.genre_list=["action","drama","romance"]
	def input(self):
		print("INPUT NAME:", end=' ')
		self.name=input()
		print("INPUT GENRE RATING:")
		for i in range(len(self.genre_list)): 		
			print("INPUT {0} RATING:".format(self.genre_list[i]), end=' ')
			self.genre_rating[self.genre_list[i]]=input()	
		overall_genre=sorted(genre_rating)[0]		
		print("INPUT RELEASE YEAR:", end=' ')
		self.release_year=input()
		print("INPUT OVERALL RATING:", end=' ')
		self.rating_overall=input()
	def __str__(self):
		return("NAME: {0}\tRELEASE YEAR: {1}\tOVERALL RATING: {2}\t OVERALL GENRE:{3} \n {4}".format(self.name,self.release_year,self.rating_overall,self.overall_genre,str(self.genre_rating)))


def movie_compare(p):
	return p.rating_overall
class ActionMovie(movie):
	def __init__(self):
		super().__init__()
		self.genre_list=["action"]	

class DramaMovie(movie):
	def __init__(self):
		super().__init__()
		self.genre_list=["drama"]

class RomanceMovie(movie):
	def __init__(self):
		super().__init__()
		self.genre_list=["romance"]