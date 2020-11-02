import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.tralier_youtube_url = trailer_youtube
    
    def trailer(self):
        webbrowser.open(self.tralier_youtube_url)