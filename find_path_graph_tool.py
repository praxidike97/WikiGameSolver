import os
import argparse
import pickle

import graph_tool
import graph_tool.topology


def find_path(input_path: str, start_article: str, end_article: str):
    title_to_index_dict = pickle.load(open(os.path.join(input_path, 'title_to_index_dict.pickle'), 'rb'))
    source = title_to_index_dict[start_article]
    target = title_to_index_dict[end_article]

    G = pickle.load(open(os.path.join(input_path, 'wiki_graph.pickle'), 'rb'))

    vertex_list, _ = graph_tool.topology.shortest_path(G, source, target)
    
    print("Result:")

    for vertex in vertex_list:
        name = list(title_to_index_dict.keys())[list(title_to_index_dict.values()).index(G.vertex_index[vertex])]
        print(name)

    print("---------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Finds paths between two articles')
    parser.add_argument('-i', '--input_path', type=str, help='The dir where the wiki graph is')
    parser.add_argument('-s', '--start', type=str, help='Which article to start from')
    parser.add_argument('-e', '--end', type=str, help='Which article to go to')

    args = parser.parse_args()

    find_path(args.input_path, args.start, args.end)
