'''
Pull down the imbd_movies dataset here and save to /data as imdb_movies_2000to2022.prolific.json
You will run this project from main.py, so need to set things up accordingly
'''

import json
from analysis_network_centrality import analyze_network_centrality
from analysis_similar_actors_genre import analyze_similar_actors_genre
import requests

# Ingest and save the imbd_movies dataset
def ingest():
    url = "https://raw.githubusercontent.com/cbuntain/umd.inst414/main/data/imdb_movies_2000to2022.prolific.json"
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/imdb_movies_2000to2022.prolific.json', 'w') as file:
            file.write(response.text)
        print("Dataset saved successfully.") #check to make sure save happened
    


# Call functions / instanciate objects from the two analysis .py files
def main():
    ingest()
    with open('data/imdb_movies_2000to2022.prolific.json', 'r') as file:
        movies = [json.loads(line) for line in file]
        
    analyze_network_centrality(movies)
    analyze_similar_actors_genre(movies)




if __name__ == "__main__":
    main()