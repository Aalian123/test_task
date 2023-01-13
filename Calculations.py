import emoji
# for calculating results


class Calculation:
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
        avg_rating = (sum(rating) / len(rating))
        return [movie_name[0], movie_name[-1], avg_rating]

    # Function for finding the total number of movies and Average mean rating
    def genr(self, gen=None):
        movies_objects = self.objects
        movies_length = 0
        sum_of_rating = 0
        for data in movies_objects:
            if gen in data.genre:
                movies_length += 1
                sum_of_rating += data.rating
        mean_rating = (sum_of_rating / movies_length) if movies_length>0 else 0
        return [movies_length, mean_rating]

    # Function for printing top 10 rated movie in gien year and printing smily
    def top_rated(self, year=None):
        movies_objects = self.objects
        results = {}
        for data in movies_objects:
            if data.year == year:
                results[data.title] = data.votes

        sort = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)[:10])
        movie_name = list(sort.keys())
        likes = list(sort.values())
        smily = round(likes[0]/len(likes))
        return [movie_name[0], likes[0], smily*emoji.emojize(":smiling_face:")]
