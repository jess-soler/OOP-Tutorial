"""
    name: movie_class.py
    author: Jessica Soler
    created: 3/28/24
    assignment: 7.3 OOP Tutorial
    puprose: use @property Pythonic way of accessing attributes
"""

class Movie:
    
    def __init__(self, title, rating):
        self._title = title
        self._rating = rating
        
    """ define getter with @property decorator"""
    @property
    def rating(self):
        
        """ get the movie rating """
        print("Calling the rating getter...")
        return self._rating
    
    """ define setter with @property.setter decorator"""
    @rating.setter
    def rating(self, new_rating: float):
        
        """ set the movie rating """
        print("Calling the rating setter...")
       
        # data validation
        # rating must be between 1.0 and 5.0
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")
            
    """ define getter with @property decorator"""
    @property
    def title(self):
            
        """ get the movie title """
        print("Calling the title getter...")
        return self._title
        
    """ define setter with @property.setter decorator """
    @title.setter
    def title(self, new_title: str):
            
        """ set the movie title """
        print("Calling the title setter...")
        self._rating = new_title
        
favorite_movie = Movie("Titanic", 4.3)
print(f"The {favorite_movie.title} has a {favorite_movie.rating} rating.\n")

favorite_movie.rating = 4.5
print(f"The {favorite_movie.title} has a {favorite_movie.rating} rating.\n")

favorite_movie.rating = -5.6 # invalid value
print(f"The {favorite_movie.title} has a {favorite_movie.rating} rating.\n")


