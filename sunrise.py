import webbrowser
class Sunrise():
    def __init__(self, sunrise_title, sunrise_image, sunrise_video_link):
        self.title = sunrise_title
        self.poster_image_url = sunrise_image
        self.trailer_youtube_url = sunrise_video_link

    def show_sunrise(self):
        webbrowser.open(self.trailer_youtube_url)
