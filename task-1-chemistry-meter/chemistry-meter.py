import imdb

db = imdb.IMDb()


actor_1 = 'gal gadot'
actor_2 = 'chris pine'

actor1 = db.search_person(actor_1)[0]
actor2 = db.search_person(actor_2)[0]
# print(actor1.getID(), actor2.getID())

actor1_movies = []
actor2_movies = []

actor1_details = db.get_person(actor1.getID(), info=['filmography'])
# print(actor1_details.keys())
# print(actor1_details['filmography']['actress'])
for actor1_movie in actor1_details['filmography']['actress']:
    actor1_movies.append(actor1_movie)

actor2_details = db.get_person(actor2.getID(), info=['filmography'])
for actor2_movie in actor2_details['filmography']['actor']:
    actor2_movies.append(actor2_movie)

for movie_1 in actor1_movies:
    print(movie_1)
print("==========================================")
for movie_2 in actor2_movies:
    print(movie_2)

