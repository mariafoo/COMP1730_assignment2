COMP1730 ASSIGNMENT2
====================

In computer science and discrete mathematics, a graph is a structure that consists of a set of nodes and a set of connections between pairs of nodes, called links. (Sometimes other names are used, e.g., 'vertex' and 'edge'. We will call them nodes and links.) Here is an example of a graph (it is test_graph_1 in the test data below):

The set of nodes is {0,1,2,3,4,5}. The links are the pairs (0,1), (0,4), (1,2), (1,4), (2,3), (3,4) and (3,5). (This is an undirected graph, meaning that if there is link from node I to node J there is also a link from J to I. Thus, the list of links also implicitly includes all reverse pairs.) For an introduction to graphs, see for example the wikipedia page "Graph_(mathematics)".

In this assignment, you will implement three functions that work on graphs. Your functions will be used by a program that we provide. Your functions will need to work with a data structure (called an "adjacency list" or "neighbour list") that represents a graph. We define this data structure below. Important, because your functions have to interoperate with the code we provided, you can not make up your own data structure.

Data Structures:

* Adjacency List -> [{a, b}, {a, c}, {b, c}]

Implement 3 functions.