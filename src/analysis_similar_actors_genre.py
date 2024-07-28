'''
PART 2: SIMILAR ACTROS BY GENRE
Using the imbd_movies dataset:
- Create a data frame, where each row corresponds to an actor, each column represents a genre, and each cell captures how many times that row's actor has appeared in that column’s genre 
- Using this data frame as your “feature matrix”, select an actor (called your “query”) for whom you want to find the top 10 most similar actors based on the genres in which they’ve starred 
- - As an example, select the row from your data frame associated with Chris Hemsworth, actor ID “nm1165110”, as your “query” actor
- Use sklearn.metrics.DistanceMetric to calculate the euclidean distances between your query actor and all other actors based on their genre appearances
- - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html
- Output a CSV continaing the top ten actors most similar to your query actor using cosine distance 
- - Name it 'similar_actors_genre_{current_datetime}.csv' to `/data`
- - For example, the top 10 for Chris Hemsworth are:  
        nm1165110 Chris Hemsworth
        nm0000129 Tom Cruise
        nm0147147 Henry Cavill
        nm0829032 Ray Stevenson
        nm5899377 Tiger Shroff
        nm1679372 Sudeep
        nm0003244 Jordi Mollà
        nm0636280 Richard Norton
        nm0607884 Mark Mortimer
        nm2018237 Taylor Kitsch
- Describe in a print() statement how this list changes based on Euclidean distance
- Make sure your code is in line with the standards we're using in this class
'''

#Write your code below
import pandas as pd
from sklearn.metrics import pairwise_distances
from datetime import datetime

def analyze_similar_actors_genre(movies):
    # Create a dictionary to hold genre counts for each actor
    actor_genres = {}

    # Process each movie in the JSON data
    for movie in movies:
        genres = movie['genres']
        actors = movie['actors']

        for actor_id, actor_name in actors:
            if actor_id not in actor_genres:
                actor_genres[actor_id] = {'name': actor_name}
            for genre in genres:
                if genre not in actor_genres[actor_id]:
                    actor_genres[actor_id][genre] = 0
                actor_genres[actor_id][genre] += 1

    # Convert the dictionary to a DataFrame
    actor_genres_df = pd.DataFrame.from_dict(actor_genres, orient='index').fillna(0)

    # Extract actor names for reference
    actor_names = actor_genres_df['name']
    actor_genres_df = actor_genres_df.drop(columns=['name'])

    # Select the query actor
    query_actor_id = 'nm0001002'  # Dean Cain

    # Calculate Cosine distances
    distances = pairwise_distances(actor_genres_df, metric='cosine')
    distances_df = pd.DataFrame(distances, index=actor_genres_df.index, columns=actor_genres_df.index)

    # Get the top 10 most similar actors based on Cosine distance
    similar_actors = distances_df[query_actor_id].sort_values()[1:11]
    top_10_actors = actor_names.loc[similar_actors.index]

    # Output the results to a CSV file
    current_datetime = datetime.now()
    csv_filename = f'data/similar_actors_genre_{current_datetime}.csv'
    top_10_actors.to_csv(csv_filename, header=False)
    

    # Print the top 10 actors
    print("Top 10 actors similar to Dean Cain based on Cosine distance:")
    for actor_id in top_10_actors.index:
        print(actor_id, top_10_actors[actor_id])
