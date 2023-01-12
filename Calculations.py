# for calculating results
class Calc:
    def __init__(self, objects):
        self.objects = objects

    # Function for calculating top and low rated movie in given year and average runtime minutes
    def find_top_low_rated(self, year=None):
        movies_objects = self.objects
        results = {}
        for data in movies_objects:
            if data.year == year:
                results[data.title] = data.rating
        sort = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)[:10])
        movie_name = list(sort.keys())
        rating = list(sort.values())
        return f"Highest rating movie is : {movie_name[0]}\nLowest rating movie is : {movie_name[-1]}\n" \
               f"Avg time is :{sum(rating) / len(rating)}"

    # Function for finding the total number of movies and Average mean rating
    def genr(self, gen=None):
        movies_objects = self.objects
        i = 0
        mean_rating = []
        for data in movies_objects:
            if data.genre == gen:
                i += 1
                mean_rating.append(data.rating)
        return f'Total No of Movies: {i} \n Mean rating is : {sum(mean_rating) / len(mean_rating)}'

    # Function for printing top 10 rated movie in gien year and printing smily
    def top_rated(self, year=None):
        movies_objects = self.objects
        results = {}
        for data in movies_objects:
            if data.year == year:
                results[data.title] = data.rating
        sort = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)[:10])
        movie_name = list(sort.keys())
        likes = list(sort.values())
        return f'Highest movie is : {movie_name[0]} \nRating is : {likes[0]}\n{round(likes[0]/len(likes))*"😊"}'
