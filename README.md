# WikiGameSolver

## Installation
The most popular Python graph library, ```networkx```, is not efficient enough to perform this task, therefore ```graph-tool``` is used (see [https://graph-tool.skewed.de/](https://graph-tool.skewed.de/)). According to the documentation it should be installable via ```apt```, but somehow this does not work/is not available. Other option: install ```homebrew``` and install it there (see [https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions#installation-via-package-managers](https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions#installation-via-package-managers)).

## Usage
The wikipedia articles are downloaded via [WikiExtractor](https://github.com/attardi/wikiextractor). See the instructions there. 

First, run 

```python build_network_graph_tool.py -i <dir with the extracted wiki articles> -o <dir to store the constructed graph>``` 

to build the graph, then use

```python find_path_graph_tool.py -i <dir where the graph is located> -s <start article> -e <end article>``` 

to find the shortest path between two articles. 

*Important*: the script is not guaranteed to find a result (or a right result for that matter). Major problem is when the article name is different from the link to the article (but cannot be bothered to fix it, as it works most of the times).
