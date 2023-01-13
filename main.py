# main file
from Parsing import Parse
from Calculations import Calculation
from Results import Result
import argparse


# main function
def main():
    path = r'Book1.csv'
    parse = Parse(path)
    parse.parse_data()
    movies_info = parse.get_movies_info()
    results = Calculation(movies_info)
    movies_object = Result()

    # =====================================
    # Command line argument parsing methods
    # =====================================

    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, help="Top 10 results against given year", default=None)
    parser.add_argument("--genre", type=str, help="Total Number of movies against given Genre", default=None)
    parser.add_argument("--topandlow", type=int, help="Top and lowest rating movie in given year", default=None)
    args = parser.parse_args()
    print(args)
    if args.topandlow:
        movies_object.set_to_and_low(results.find_top_low_rated(args.topandlow))
        print(movies_object.get_top_and_low())
    if args.genre:
        movies_object.set_genre(results.genr(args.genre))
        print(movies_object.get_genre())
    if args.top:
        movies_object.set_top_rated(results.top_rated(args.top))
        print(movies_object.get_top_rated())


if __name__ == '__main__':
    main()
