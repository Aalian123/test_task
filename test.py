# def rating(self, rating=5.6, year=1894,name =None,):
#     counter = 0
#     movies_data = Parse.get_data('Book1.csv')
#     list = []
#     if year:
#         for i in range(1, len(movies_data)-1):
#             result = {}
#             for key, value in movies_data[i].items():
#                 print(value)
#                 if movies_data[i]['rating'] == str(rating) or movies_data[i]['startYear'] == str(year):
#                     result.update(rating=rating, year=year, Movie_name=movies_data[i]['originalTitle'])
#                     # result[movies_data[i][key]] = rating
#                     # result[movies_data[i]['startYear']] = year
#                     list.append(result)
#                     counter += 1
#
#     else:
#         for i in range(1, len(movies_data)):
#             result = {}
#             for key, value in movies_data[i].items():
#                 print(value)
#                 if value == str(rating):
#                     result[movies_data[i]['originalTitle']] = value
#                     list.append(result)
#                     counter += 1
#
#     return list, f'total Movies {counter}'