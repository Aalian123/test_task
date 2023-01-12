# main file
from Parsing import Parse
from Calculations import Calc
import argparse


# main function
def main():
    path = r'Book1.csv'
    parse = Parse(path)
    movies_data = parse.get_data()
    results = Calc(movies_data)

    # =====================================
    # Command line argument parsing methods
    # =====================================

    parser = argparse.ArgumentParser()
    group = parser.add_subparsers(dest='command')
    call = group.add_parser("call")
    call.add_argument("--top", type=int)
    call.add_argument("--genre", type=str)
    call.add_argument("--topandlow", type=int)
    args = parser.parse_args()

    if args.command == 'call':
        if args.topandlow:
            print(results.find_top_low_rated(args.topandlow))
        if args.genre:
            print(results.genr(args.genre))
        if args.top:
            print(results.top_rated(args.top))


if __name__ == '__main__':
    main()
