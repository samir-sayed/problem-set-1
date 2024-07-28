'''
PART 1: NETWORK CENTRALITY METRICS

Using the imbd_movies dataset
- Guild a graph and perform some rudimentary graph analysis, extracting centrality metrics from it. 
- Below is some basic code scaffolding that you will need to add to. 
- Tailor this code scaffolding and its stucture to however works to answer the problem
- Make sure the code is line with the standards we're using in this class 
'''

import numpy as np
import pandas as pd
import networkx as nx
import requests
import json
from datetime import datetime

def analyze_network_centrality(movies): 
    url = "https://raw.githubusercontent.com/cbuntain/umd.inst414/main/data/imdb_movies_2000to2022.prolific.json"

    response = requests.get(url)
    with open('imdb_movies_2000to2022.json', 'w') as file:
        file.write(response.text)

    # Build the graph
    g = nx.Graph()

    # Set up your dataframe(s) -> the df that's output to a CSV should include at least the columns 'left_actor_name', '<->', 'right_actor_name'
    df = []

    with open('imdb_movies_2000to2022.json', 'r') as in_file:
        #iterate through data, isolate actors and seperate them by first/last name
        
        
        for line in in_file:
            this_movie = json.loads(line)
        
            for actor_id, actor_name in this_movie['actors']:
                g.add_node(actor_id, name = actor_name)
            i = 0
            for left_actor_id, left_actor_name in this_movie['actors']:
                for right_actor_id, right_actor_name in this_movie['actors'][i+1:]:
                    if g.has_edge(left_actor_id, right_actor_id):
                        g[left_actor_id][right_actor_id]['weight'] += 1
                    else:
                        g.add_edge(left_actor_id, right_actor_id, weight = 1)
                        df.append({'left_actor_name': left_actor_name, '<->': '<->', 'right_actor_name': right_actor_name})
                i += 1


    # Print the info below
    print("Nodes:", len(g.nodes))
    print("Edges:", len(g.edges))

    #Print the 10 the most central nodes
    degree_centrality = nx.degree_centrality(g)
    ten_degree = sorted(degree_centrality.items(), key = lambda x: x[1], reverse=True)[:10]

    # Output the final dataframe to a CSV named 'network_centrality_{current_datetime}.csv' to `/data`
    actor_df = pd.DataFrame(df)
    current_datetime = datetime.now()
    csv_file = f'network_centrality_{current_datetime}.csv'
    actor_df.to_csv(csv_file, index=False)
    print(f'Dataframe saved')

