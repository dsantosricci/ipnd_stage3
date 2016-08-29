import webbrowser

#This class is used to process some repetitive information 
class Movie():
	""" This class provides a way to store movie related information"""
	#this function __init__ takes some informations about the movie as its input and returns an organized structure to store its data. The init method is called a constructor for a class.
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	#show_trailer is a function that is used to open a web browser. It takes the trailer_youtube_url and returns a web browser showing the trailer on youtube
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


		
		
