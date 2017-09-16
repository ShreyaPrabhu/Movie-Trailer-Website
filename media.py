import webbrowser
# Import webbrowser module to open web links to show trailers

# Create a class called Movie


class Movie:

    # Constructor for the class Movie
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to show trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
