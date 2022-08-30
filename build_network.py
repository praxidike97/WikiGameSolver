import argparse
import os
import json
import re
import pickle
import sys

import networkx as nx
from tqdm import tqdm
from guppy import hpy


def build_network(input_dir: str, store_path: str):
    if not os.path.isdir(input_dir):
        return

    G = nx.DiGraph()
    h = hpy()

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

                if title not in G.nodes:
                    G.add_node(title)

                for match in re.finditer(r"href=\"(.*?)(/a&gt)", text):
                    split_match = match.group().split(";")

                    link_text = split_match[1].split("&")[0]
                    #link = split_match[0].split("\"")[1]

                    if link_text not in G.nodes:
                        G.add_node(link_text)

                    G.add_edge(title, link_text)

            f.close()

        print(h.heap())
        #if dir_name == "DA":
        #    break

        pickle.dump(G, open(os.path.join(store_path, 'wiki_graph.pickle'), 'wb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Builds a network from the extracted articles')
    parser.add_argument('-i', '--input', type=str, help='The directory with the extracted articels where to build a graph from')
    parser.add_argument('-o', '--output', type=str, help='THe directory to store the graph')
    #parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                const=sum, default=max,
    #                help='sum the integers (default: find the max)')

    args = parser.parse_args()

    build_network(args.input, args.output)
