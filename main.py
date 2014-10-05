
from assign2 import read_graph_from_file
from assign2 import label_graph_components
from assign2 import get_component_density
from assign2 import FileFormatError

from drawing import show_graph

# ask user for a file name
graph_file_name = input("Enter graph file name: ")

try:
    # read a graph from this file
    (g_link_list, g_position_list) = read_graph_from_file(graph_file_name)

    # display the graph
    show_graph(g_link_list, g_position_list, title_str="Input graph")

    # calculate connected components
    g_label_list = label_graph_components(g_link_list)

    # display graph with components
    show_graph(g_link_list, g_position_list,
               title_str="Labelled graph", label_list=g_label_list)

    # calculate and print density for each component in the graph
    for label in range(max(g_label_list) + 1):
        density = get_component_density(label, g_link_list, g_label_list)
        print("density in component {} is {:.2f}".format(label, density))

except FileFormatError as ffe:
    print("Invalid graph file: " + str(ffe))

except Exception as exc:
    print("An error occurred: " + str(exc))
