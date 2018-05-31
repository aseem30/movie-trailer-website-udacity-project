''' Defines the Movie class that contains the details of a movie.'''
import webbrowser
''' This class provides a way to store movie related information.'''


class Movie():
    def __init__(self, title, poster_image_url, trailer_youtube, storyline):
        ''' Initialises Movie class instance variables.'''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube
        self.storyline = storyline

    def show_trailer(self):
        ''' Plays the movie trailer in the web browser.'''
        webbrowser.open(self.trailer_youtube_url)
