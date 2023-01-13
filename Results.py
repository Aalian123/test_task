class Result:
    def __init__(self):
        self.top_and_low = {}
        self.genre = {}
        self.top_rated = {}

    def set_to_and_low(self, values):
        self.top_and_low["Top rated Movie is "] = values[0]
        self.top_and_low["Lower rated movie "] = values[1]
        self.top_and_low["Average rating is "] = values[2]

    def set_genre(self, values):
        self.genre["movie_length"] = values[0]
        self.genre["Mean Rating is"] = values[1]

    def set_top_rated(self, values):
        self.top_rated["Top rated movie is "] = values[0]
        self.top_rated["No of votes "] = values[1]
        self.top_rated["smily"] = values[2]

    def get_top_and_low(self):
        return self.top_and_low

    def get_genre(self):
        return self.genre

    def get_top_rated(self):
        return self.top_rated
