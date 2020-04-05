import webbrowser


class Movie():
    """ This Provides you with the documentation for the website program,
        it is part of the Movie Trailer Website Project and is part of the
        set of projects of the Nano Degree Fullstack course """

    # The __init__ function defines what variables 
    # each instance of the class Movie will have.
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function opens webbrowser window and plays the movie trailer 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
