from csv       import reader
from itertools import groupby
from operator  import itemgetter

def rating_high_or_low_flag( (movie_name, rating) ):
    high_low_flag = 'invalid'
    if rating > 3.5: high_low_flag = 'h'
    if rating < 2.5: high_low_flag = 'l'
    return (movie_name, high_low_flag)

csv_reader_existing = reader(open('existing.db.txt', 'r'), delimiter=';')

existing_ratings = []
for row in csv_reader_existing:
    existing_ratings.append( ( int(row[0]), row[1], float(row[2]) ) )

sorted_existing_ratings = sorted( existing_ratings )

#print sorted_existing_ratings

existing_ratings_grouped_by_user_id = []
for k, g in groupby(sorted_existing_ratings, lambda x: x[0]):
    existing_ratings_grouped_by_user_id.append(list(g))

#print existing_ratings_grouped_by_user_id

raw_recommendations_list = []
for ratings_group in existing_ratings_grouped_by_user_id:
    raw_recommendations_list += \
      [ ( rating_high_or_low_flag( ( tpl1[1], tpl1[2] ) ), ( tpl2[1], tpl2[2] ) )
        for tpl1 in ratings_group
        for tpl2 in ratings_group
        if tpl1 != tpl2 and tpl2[2] > 3.5
      ]

#print raw_recommendations_list

existing_dict = {}
for tpl in raw_recommendations_list:
    existing_dict[tpl[0]] = existing_dict.get(tpl[0], []) + [tpl[1]]

#print existing_dict

csv_reader_new = reader(open('new.db.txt', 'r'), delimiter=';')

fresh_ratings = []
for row in csv_reader_new:
    tpl = ( row[0], float(row[1]) )
    fresh_ratings.append( rating_high_or_low_flag( tpl ) )

#print fresh_ratings

intermediate_step_recommendations_list = []
for fresh_rating in fresh_ratings:
    intermediate_step_recommendations_list += existing_dict[fresh_rating]

#print intermediate_step_recommendations_list

recommendations_dict = {}
for tpl in intermediate_step_recommendations_list:
    recommendations_dict[tpl[0]] = recommendations_dict.get(tpl[0], 0.0) + tpl[1]

for fr in fresh_ratings:
    already_watched_movie = fr[0]
    if already_watched_movie in recommendations_dict:
        del recommendations_dict[already_watched_movie]

#print recommendations_dict

recommendations_ordered_by_most_relevant_first = \
    sorted( recommendations_dict.items(),
            key=itemgetter(1),
            reverse=True )

#print recommendations_ordered_by_most_relevant_first

print ''

print 'We recommend you watch the following movies:'

print ''

for tpl in recommendations_ordered_by_most_relevant_first:
    print tpl[0]

print ''


