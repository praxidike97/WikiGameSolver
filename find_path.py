import argparse
import pickle

import networkx as nx


def find_path(input_file: str, start_article: str, end_article: str):
    G = pickle.load(open(input_file, 'rb'))

    #for node in G.nodes:
    #    print(node)

    #print(G.in_edges("Adolf Hitler"))
    print(nx.shortest_path(G, start_article, end_article))
    #print(G.nodes["Adolf%20Hitler"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Finds paths between two articles')
    parser.add_argument('-i', '--input', type=str, help='The file where the wiki graph is')
    parser.add_argument('-s', '--start', type=str, help='Which article to start from')
    parser.add_argument('-e', '--end', type=str, help='Which article to go to')

    args = parser.parse_args()

    find_path(args.input, args.start, args.end)
