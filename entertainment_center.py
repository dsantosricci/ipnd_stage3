# This code takes four movies as its input and returns in a webpage these four movies with a cover image and trailer. 

# Fresh_tomatoes is used for opening the web-page and displaying the four movies
import fresh_tomatoes

# Media is used to store the classes we use here.	
import media

# Here are my four favourite movies
youth = media.Movie("Youth", "A retired orchestra conductor is on holiday with his daughter and his film director best friend in the Alps when he receives an invitation from Queen Elizabeth II to perform for Prince Philip's birthday.", "https://www.cinematerial.com/media/posters/md/tj/tjwjlcul.jpg?v=1456370670", "https://www.youtube.com/watch?v=-T7CM4di_0c")
once = media.Movie("Once upon a time in America", "A former Prohibition-era Jewish gangster returns to the Lower East Side of Manhattan over thirty years later, where he once again must confront the ghosts and regrets of his old life.", "http://www.publispain.com/posters/once_upon_a_time_in_america.jpg", "https://www.youtube.com/watch?v=Jj5Xczethmw")
shaw = media.Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
victoria = media.Movie("Victoria", "A young Spanish woman who has newly moved to Berlin finds her flirtation with a local guy turn potentially deadly as their night out with his friends reveals a dangerous secret.", "http://redcarpetcrash.com/wp-content/uploads/2015/07/victoria.jpg", "https://www.youtube.com/watch?v=eUmrewmeOCQ")




movies = [youth, victoria, shaw, once]

fresh_tomatoes.open_movies_page(movies)

