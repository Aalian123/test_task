import csv
import Movies


# loading data
class Parse:

    movies_info = []

    def __init__(self, path):
        self.path = path

    # Funtion for getting and parsing data from csv file
    def parse_data(self):
        with open(self.path, encoding='utf-8') as csv_file:
            workbook = csv.reader(csv_file)
            next(workbook)
            for row in workbook:
                idd = row[0]
                typee = row[1]
                title = row[2]

                row[3] = 0 if row[3] == '\\N' else row[3]
                year = row[3]

                row[4] = 0 if row[4] == '\\N' else row[4]
                runtime = row[4]
                genre = row[5]

                rating = row[6]
                votes = row[7]

                movie_object = Movies.Movies(idd, typee, title, year, runtime, genre, rating, votes)
                self.movies_info.append(movie_object)

    def get_movies_info(self):
        return self.movies_info
