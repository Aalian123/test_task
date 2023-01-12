# for holding movie data
class Movies:
    def __init__(self, id, Type, title, year, runtime, genre, rating, votes):
        self.id = id
        self.type = Type
        self.title = title
        self.year = int(year)
        self.runtime = int(runtime)
        self.genre = genre
        self.rating = float(rating)
        self.votes = float(votes)

    # Funtion for returning Data
    def __str__(self):
        return self.id, self.Type, self.title, self.year, self.runtime, self.genre, self.rating, self.votes
