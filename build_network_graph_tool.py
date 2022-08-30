import argparse
import os
import json
import re
import pickle

import graph_tool
from tqdm import tqdm


def build_network(input_dir: str, store_path: str):
    title_to_index_dict = dict()
    current_idx = 0

    if not os.path.isdir(input_dir):
        return

    print("Before G")
    G = graph_tool.Graph(directed=True)
    print("After G")

    for dir_name in tqdm(os.listdir(path=input_dir)):
        print(f"dir_name: {dir_name}")

        for file_name in tqdm(os.listdir(os.path.join(input_dir, dir_name))):
            f = open(os.path.join(input_dir, dir_name, file_name))
            lines = f.readlines()

            for line in lines:
                data = json.loads(line)

                if data['text'] == '':
                    continue

                text = data['text']
                title = data['title']

                if title not in title_to_index_dict:
                    title_to_index_dict[title] = current_idx
                    G.add_vertex()
                    current_idx += 1

                for match in re.finditer(r"href=\"(.*?)(/a&gt)", text):
                    split_match = match.group().split(";")

                    link_text = split_match[1].split("&")[0]
                    #link = split_match[0].split("\"")[1]

                    if link_text not in title_to_index_dict:
                        title_to_index_dict[link_text] = current_idx
                        G.add_vertex()
                        current_idx += 1

                    G.add_edge(title_to_index_dict[title], title_to_index_dict[link_text])

            f.close()

        pickle.dump(G, open(os.path.join(store_path, 'wiki_graph.pickle'), 'wb'))
        pickle.dump(title_to_index_dict, open(os.path.join(store_path, 'title_to_index_dict.pickle'), 'wb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Builds a network from the extracted articles')
    parser.add_argument('-i', '--input', type=str, help='The directory with the extracted articels where to build a graph from')
    parser.add_argument('-o', '--output', type=str, help='The directory to store the graph')
    #parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                const=sum, default=max,
    #                help='sum the integers (default: find the max)')

    args = parser.parse_args()

    build_network(args.input, args.output)
